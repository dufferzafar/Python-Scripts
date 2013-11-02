import os
import urllib.parse
import xml.etree.ElementTree as ET

# import subprocess

import HelperFunctions

# Script Mode
# list / playlist
mode = "playlist"

# The artist to look for
artist = "Explosions in the sky"

# Number of tracks to download
limit = "20"

# Don't abuse, Please.
api_key = "da70281f2f464cfaa4638c4bfe820f9a"

# Last.fm API
root_url = "http://ws.audioscrobbler.com/2.0/?"

# Discography Folder
if mode == "playlist":
    if os.path.isdir("F:\\More Music\\" + artist):
        artistFolder = "F:\\More Music\\" + artist
    elif os.path.isdir("G:\\Music\\" + artist):
        artistFolder = "G:\\Music\\" + artist
    else:
        print("Where to look for music files?")
        quit()

# The file where lastfm response will be saved
fileName = "Artists\\" + artist + " - Top " + limit + ".xml"

print("Downloading File... " + artist)

# Download to file
params = urllib.parse.urlencode({'method': 'artist.gettoptracks', 'artist': artist, 'api_key': api_key, 'limit': limit})
HelperFunctions.downloadToFile(root_url+params, fileName)

# Build a parse tree
tree = ET.parse(fileName).find("toptracks")
# Decide what to do
if mode == "list":
    # os.system('clear')
    # subprocess.call("cls", shell=True) # windows

    for item in tree.findall("track"):
        track = item.find("name").text
        playcount = item.find("playcount").text
        listeners = item.find("listeners").text
        print(track, playcount, listeners)

elif mode == "playlist":
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

    # Play Some Music!!
    # os.startfile(playlist)

# Whew!!
# print("All Done!")
