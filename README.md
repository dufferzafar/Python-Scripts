# Python-Scripts

After some initial reluctance, I've finally begun to code in Python.

Here are some of the scripts I've managed to write. Most of them are 'quick-and-dirty' and were created for a very specific use-case, so they may not be of much use as-is. But you are free to edit any of them to suit your needs.

## List of scripts

* [0xMirror](#mirror)
* [Batch Edit MP3 Metadata](#meta)
* [Goodreads Quotes](#gr)
* [Imgur Uploader](#imgur)
* [Last.fm](#lfm)
* [MITx Solutions](#mitx)
* [MusicBrainz IRC Chatlogs Downloader](#irc)
* [Networx XML Parser](#networx)
* [Sublime Text 3 Plugins](#sublime)
* [WP XML to Octopress MD](#wp)

# <a name="mirror"></a>0xMirror

A script to create a zero-byte mirror of an entire hard disk.

**Tech:** scandir

# <a name="gr"></a>Goodreads Quotes

A script to download all the quotes I've liked on Goodreads. The plan was to create a offline database that I could edit.

Couldn't decide how/what to do. So this is just half-done.

**Tech:** BeautifulSoup to parse the webpage downloaded.

# <a name="imgur"></a>Imgur Uploader

Uploads an image to Imgur hosting service. Nothing Concrete.

I needed an uploader to share screenshots that I grab - Python seemed a bad option. So I created an Autohotkey version - see [Win-Butler](https://github.com/dufferzafar/win-butler).

**Tech:** PyImgur

# <a name="lfm"></a>Last.fm

I am an avid user of the last.fm service. These scripts interact with last.fm's API.

**TopTracks.py**

Creates a local playlist from Top 20 tracks of an artist. 

Useful when you have a huge collection of songs and you can't decide what to listen to.

**ScrobblesToday.py**

View the number of songs you have listened to today.

**Tech:** Parse XML responses from the API. os.Walk() to find mp3 files matching the criteria.

# <a name="mitx"></a>MITx Solutions

Set of solutions to the 6.00.1x course from EdX.

https://courses.edx.org/courses/MITx/6.00.1x/3T2013/courseware/

I left the course in between, as I often do.
 
# <a name="networx"></a>Networx XML Parser

Parses [Networx](http://www.softperfect.com/products/networx) backup XMLs and outputs the data in js format. 

**Tech:** datetime module. XML parsing.

This script has been moved to a new repository - [Internet-Usage](http://github.com/dufferzafar/internet-usage).

# <a name="wp"></a>WP XML to Octopress MD

I used this script to shift my blog from Wordpress to Octopress.

It creates individual blog posts in markdown format from a wordpress export file (XML).

**Tech:** XML Parsing. Namespace Dictionaries.

# <a name="sublime"></a>Sublime Text 3 Plugins

Small Plugins that I've written/copied for sublime text.

# <a name="meta"></a>Batch Edit MP3 Metadata

Use Mutagen to modify artist tag of multiple mp3 files.

**Tech:** Mutagen.

# <a name="irc"></a>MusicBrainz IRC Chatlogs Downloader

Script used to download IRC Chatlogs of #musicbrainz and #musicbrainz-devel.

