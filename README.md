# Python-Scripts

After some initial reluctance, I've finally begun to code in Python.

Here are the scripts I've managed to write.

## List of scripts

* [Goodreads Quotes](#gr)
* [Imgur Uploader](#imgur)
* [Last.fm](#lfm)
* [MITx Solutions](#mitx)
* [Networx XML Parser](#networx)
* [WP XML to Octopress MD](#wp)
* [Sublime Text 3 Plugins](#sublime)

# <a name="gr"></a>Goodreads Quotes

A script to download all the quotes I've liked on Goodreads. The plan was to create a offline database that I could edit.

Couldn't decide how/what to do. So this is just half-done.

**Tech:** BeautifulSoup to parse the webpage downloaded.

# <a name="imgur"></a>Imgur Uploader

Uploads an image to Imgur hosting service. Nothing Concrete.

I needed an uploader to share screenshots that I grab - Python seemed a bad option. So as of 05/11/2013 I'm working on an Autohotkey version.

**Tech:** Uses PyImgur.

# <a name="lfm"></a>Last.fm

I am an avid user of the last.fm service. These service interact with last.fm's API.

**TopTracks.py**

Creates a local playlist from Top 20 tracks of an artist. 

Useful when you have a huge collection of songs and you just can't decide what to listen to.

**ScrobblesToday.py**

View the number of songs you have listened to today.

**Tech:** Parse XML responses from the API. os.Walk() to find mp3 files matching the criteria.

# <a name="mitx"></a>MITx Solutions

Set of solutions to the 6.00.1x course from EdX.

https://courses.edx.org/courses/MITx/6.00.1x/3T2013/courseware/
 
# <a name="networx"></a>Networx XML Parser

Parses [Networx](http://www.softperfect.com/products/networx) backup XMLs and outputs the data in js format. 

I then used chart.js to create charts of my internet usage.

**Tech:** datetime module. XML parsing.

# <a name="wp"></a>WP XML to Octopress MD

I used this script to shift my blog from Wordpress to Octopress.

It creates individual blog posts in markdown format from a wordpress export file (XML).

**Tech:** XML Parsing. Namespace Dictionaries.

# <a name="sublime"></a>Sublime Text 3 Plugins

Small Plugins that I've written/copied for sublime text.
