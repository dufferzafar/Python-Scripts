"""
Script for exporting tracks through audioscrobbler API.

Almost of the work was originally done by the libre.fm people.
https://gitorious.org/fmthings/lasttolibre/
"""

import urllib2
import urllib

import re
import time
import xml.etree.ElementTree as ET


def connect_server(username, startpage, tracktype='recenttracks'):
    """ Connect to server and get a XML page."""
    baseurl = 'http://ws.audioscrobbler.com/2.0/?'
    urlvars = dict(method='user.get%s' % tracktype,
                   api_key='da70281f2f464cfaa4638c4bfe820f9a',
                   user=username,
                   page=startpage,
                   limit=50)

    url = baseurl + urllib.urlencode(urlvars)
    for interval in (1, 5, 10, 62, 240):
        try:
            f = urllib2.urlopen(url)
            break
        except Exception, e:
            last_exc = e
            print "Exception occured, retrying in %ds: %s" % (interval, e)
            time.sleep(interval)
    else:
        print "Failed to open page %s" % urlvars['page']
        raise last_exc

    response = f.read()
    f.close()

    # Bad hack to fix bad xml
    response = re.sub('\xef\xbf\xbe', '', response)

    # Save raw backup xmls
    # with open("XMLs/" + str(urlvars['page'])+".xml", "w") as backup:
    #     backup.write(response)

    return response


def get_pageinfo(response, tracktype='recenttracks'):
    """Check how many pages of tracks the user have."""
    xmlpage = ET.fromstring(response)
    totalpages = xmlpage.find(tracktype).attrib.get('totalPages')
    return int(totalpages)


def get_tracklist(response):
    """Read XML page and get a list of tracks and their info."""
    xmlpage = ET.fromstring(response)
    tracklist = xmlpage.getiterator('track')
    return tracklist


def parse_track(trackelement):
    """Extract info from every track entry and output to list."""
    if trackelement.find('artist').getchildren():
        # artist info is nested in loved/banned tracks xml
        artistname = trackelement.find('artist').find('name').text
        artistmbid = trackelement.find('artist').find('mbid').text
    else:
        artistname = trackelement.find('artist').text
        artistmbid = trackelement.find('artist').get('mbid')

    if trackelement.find('album') is None:
        # no album info for loved/banned tracks
        albumname = ''
        albummbid = ''
    else:
        albumname = trackelement.find('album').text
        albummbid = trackelement.find('album').get('mbid')

    trackname = trackelement.find('name').text
    trackmbid = trackelement.find('mbid').text
    date = trackelement.find('date').get('uts')

    output = [date, trackname, artistname,
              albumname, trackmbid, artistmbid, albummbid]

    for i, v in enumerate(output):
        if v is None:
            output[i] = ''

    return output


def get_tracks(username, startpage=1, tracktype='recenttracks'):
    page = startpage
    response = connect_server(username, page, tracktype)
    totalpages = get_pageinfo(response, tracktype)

    if startpage > totalpages:
        raise ValueError(
            "First is higher than total pages (%s)." % (startpage, totalpages))

    while page <= totalpages:
        # Skip connect if on first page, already have that one stored.

        if page > startpage:
            response = connect_server(username, page, tracktype)

        tracklist = get_tracklist(response)

        tracks = []
        for trackelement in tracklist:
            # do not export the currently playing track.
            if not trackelement.attrib.has_key("nowplaying") \
                    or not trackelement.attrib["nowplaying"]:
                tracks.append(parse_track(trackelement))

        yield page, totalpages, tracks

        page += 1
        time.sleep(.5)


def write_tracks(tracks, outfileobj):
    """Write tracks to an open file"""
    for fields in tracks:
        outfileobj.write(("\t".join(fields) + "\n").encode('utf-8'))


if __name__ == "__main__":
    username = "dufferzafar"
    output_file = "scrobbles-backup-year.tsv"

    # Todo: Rather than using a start page, use timestamps
    # of the already existing data to find the start/end
    startpage = 1

    # Can be used for loved/banned tracks etc.
    # Todo: Read the API and backup other stuff as well.
    infotype = "recenttracks"

    trackdict = {}
    page = startpage
    totalpages = -1

    # Key used for loved/banned
    dict_key = 0

    try:
        for page, totalpages, tracks in get_tracks(username, startpage, tracktype=infotype):
            print "Got page %s of %s.." % (page, totalpages)
            for track in tracks:
                if infotype == 'recenttracks':
                    trackdict.setdefault(track[0], track)
                else:
                    # Can not use loved/banned tracks as
                    # it's not unique
                    dict_key += 1
                    trackdict.setdefault(dict_key, track)
    except ValueError, e:
        exit(e)
    except Exception:
        raise
    finally:

        with open(output_file, 'a') as backup:

            # Newest First
            tracks = sorted(trackdict.values(), reverse=True)

            # Todo: Save this data in some better format
            write_tracks(tracks, backup)

            print "Wrote page %s-%s of %s to file %s" % (startpage, page, totalpages, output_file)
