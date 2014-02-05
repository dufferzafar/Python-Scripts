import os
import urllib.parse
import xml.etree.ElementTree as ET

import HelperFunctions

# Number of tracks to download
limit = "20"

# Don't abuse, Please.
api_key = "da70281f2f464cfaa4638c4bfe820f9a"

# Last.fm API
root_url = "http://ws.audioscrobbler.com/2.0/?"

# Discography Folder
for artist in os.listdir("G:\\Music\\#More"):
    if '#' not in artist:

        if os.path.isdir("G:\\Music\\#More\\" + artist):
            artistFolder = "G:\\Music\\#More\\" + artist
        else:
            continue

        # The file where lastfm response will be saved
        fileName = "Artists\\" + artist + " - Top " + limit + ".xml"

        print("Downloading File... " + artist)

        # Download to file
        params = urllib.parse.urlencode({'method': 'artist.gettoptracks', 'artist': artist, 'api_key': api_key, 'limit': limit})
        if (HelperFunctions.downloadToFile(root_url+params, fileName) == 0):
            print("Skipping... " + artist)
            print("=====================")
            continue

        # Build a parse tree
        tree = ET.parse(fileName).find("toptracks")

        # Output playlist file
        playlist = artistFolder + "\\" + artist + " - Top " + limit + ".m3u"
        op = open(playlist, "w")

        print("Building Playlist... " + artist)

        # Iter through the XML
        for item in tree.findall("track"):
            track = item.find("name").text

            # Walk in the directory
            for dirpath, dirnames, files in os.walk(artistFolder):
                for filename in files:
                    if track.lower() in filename.lower():
                        op.write(os.path.join(dirpath, filename))
                        op.write("\n")

        # Cleanup
        op.close()

        print("=====================")

# Whew!!
print("All Done!")
