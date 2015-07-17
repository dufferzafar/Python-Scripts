# Python-Scripts

After some initial reluctance, I've finally begun to code in Python.

Here are some of the scripts I've managed to write. Most of them are 'quick-and-dirty' and were created for a very specific use-case, so they may not be of much use as-is. But you are free to edit any of them to suit your needs.

## List of scripts

* [0xMirror](#mirror)
* [Batch Edit MP3 Metadata](#meta)
* [Find Untagged MP3s](#untagged)
* [Geeks for Geeks Scraper](#g4g)
* [Github Contributions](#github)
* [Goodreads Quotes](#gr)
* [Last.fm Plays](#lfm-plays)
* [Last.fm Backup](#lfm-backup)
* [MITx Solutions](#mitx)
* [MusicBrainz IRC Chatlogs Downloader](#irc)
* [Network Usage Analyst](#netuse)
* [Networx XML Parser](#networx)
* [Sphinx Linkfix](#linkfix)
* [Sublime Text 3 Plugins](#sublime)
* [WP XML to Octopress MD](#wp)

# <a name="mirror"></a>0xMirror

A script to create a zero-byte mirror of an entire hard disk.

**Tech:** scandir

# <a name="meta"></a>Batch Edit MP3 Metadata

Use Mutagen to modify artist tag of multiple mp3 files.

**Tech:** Mutagen.

# <a name="untagged"></a>Find Untagged MP3s

Find all songs in the current directory that have not been tagged with MusicBrainz IDs and optionally move them to a separate folder.

**Tech:** Mutagen. MBIDs.

# <a name="gr"></a>Geeks for Geeks Scraper

Create nice PDFs from posts on Geeks for Geeks.

**Tech:** BeautifulSoup, Printing html to pdf using QTextDocument.

# <a name="github"></a>Github Contributions

Fetch all previous year contributions from Github (issues, pull requests etc.)

**Tech:** Basic Web Scraping using Beautiful Soup.

# <a name="gr"></a>Goodreads Quotes

A script to download all the quotes I've liked on Goodreads. The plan was to create a offline database that I could edit.

Couldn't decide how/what to do. So this is just half-done.

**Tech:** BeautifulSoup to parse the webpage downloaded.

# <a name="lfm-backup"></a>Last.fm Backup

A script to backup my last.fm scrobbles, loved/banned tracks.

**Tech:** XML. CSV. sqlite.

# <a name="lfm-plays"></a>Last.fm Plays

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

# <a name="irc"></a>MusicBrainz IRC Chatlogs Downloader

Script used to download IRC Chatlogs of #musicbrainz and #musicbrainz-devel.

**Tech:** urllib

# <a name="networx"></a>Networx XML Parser

Parses [Networx](http://www.softperfect.com/products/networx) backup XMLs and outputs the data in js format. 

**Tech:** datetime module. XML parsing.

This script has been moved to a new repository - [Internet-Usage](http://github.com/dufferzafar/internet-usage).

# <a name="netuse"></a>Network Usage Analyst

I have a cron job setup that dumps my network usage to files. 

This script reads in those files and outputs data such as data downloaded this month, data left and suggested usage.

# <a name="linkfix"></a>Sphinx Linkfix

Uses the linkcheck's output file to fix links in docs.

Originally created for [this issue](https://github.com/scrapy/scrapy/issues/606).

# <a name="sublime"></a>Sublime Text 3 Plugins

Small Plugins that I've written/copied for sublime text.

# <a name="wp"></a>WP XML to Octopress MD

I used this script to shift my blog from Wordpress to Octopress.

It creates individual blog posts in markdown format from a wordpress export file (XML).

**Tech:** XML Parsing. Namespace Dictionaries.
