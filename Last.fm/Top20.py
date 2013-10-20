import os
import urllib.parse
import xml.etree.ElementTree as ET

import HelperFunctions

# The artist to look for
artist = "Owl City"

# Discography Folder
if os.path.isdir("F:\\More Music\\" + artist):
    artistFolder = "F:\\More Music\\" + artist
elif os.path.isdir("G:\\Music\\" + artist):
    artistFolder = "G:\\Music\\" + artist
else:
    print("Where to look for music files?")
    quit()

# Number of tracks to download
limit = "20"

# Don't abuse, Please.
api_key = "da70281f2f464cfaa4638c4bfe820f9a"

# Last.fm API
root_url = "http://ws.audioscrobbler.com/2.0/?"
params = urllib.parse.urlencode({'method': 'artist.gettoptracks', 'artist': artist, 'api_key': api_key, 'limit': limit})

# The file where lastfm response will be saved
fileName = "Artists\\" + artist + " - Top " + limit + ".xml"

print("Downloading File...")

# Download to file
HelperFunctions.downloadToFile(root_url+params, fileName)

# Build a parse tree
tree = ET.parse(fileName).find("toptracks")

# Output playlist file
playlist = artistFolder + "\\" + artist + " - Top " + limit + ".m3u"
op = open(playlist, "w")

print("Building Playlist...")

# Iter through the XML
for item in tree.findall("track"):
    track = item.find("name").text
    # print(track)

    # Walk in the directory
    for dirpath, dirnames, files in os.walk(artistFolder):
        for filename in files:
            if track.lower() in filename.lower():
                # print(filename)
                # print(os.path.join(dirpath, filename))
                op.write(os.path.join(dirpath, filename))
                op.write("\n")
                count += 1

# Cleanup
op.close()

print("All Done!")

# Play Some Music!!
os.startfile(playlist)
