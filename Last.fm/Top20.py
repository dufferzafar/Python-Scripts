# import json
import urllib.parse
import os
import xml.etree.ElementTree as ET

import HelperFunctions

# artist = "Lifehouse"
# artistFolder = "F:\More Music\Lifehouse"

artist = "God is an Astronaut"
artistFolder = "F:\More Music\God is an Astronaut"
limit = "20"

api_key = "da70281f2f464cfaa4638c4bfe820f9a"
root_url = "http://ws.audioscrobbler.com/2.0/?"

params = urllib.parse.urlencode({'method': 'artist.gettoptracks', 'artist': artist, 'api_key': api_key, 'limit': limit})

fileName = artist + " - Top " + limit + ".xml"
HelperFunctions.downloadToFile(root_url+params, fileName)

tree = ET.parse(fileName).find("toptracks")

for item in tree.findall("track"):
    # print(item.find("name").text)
    # track = "You and Me"
    track = item.find("name").text

    print(track, end=" ==> ")

    for dirpath, dirnames, files in os.walk(artistFolder):
        for filename in files:
            if track.lower() in filename.lower():
                print(filename)