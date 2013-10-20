# import json
import urllib.parse
import xml.etree.ElementTree as ET

import HelperFunctions

artist = "30 Seconds to mars"
limit = "20"

api_key = "da70281f2f464cfaa4638c4bfe820f9a"
root_url = "http://ws.audioscrobbler.com/2.0/?"

params = urllib.parse.urlencode({'method': 'artist.gettoptracks', 'artist': artist, 'api_key': api_key, 'limit': limit})

fileName = artist + " - Top " + limit + ".xml"
# HelperFunctions.downloadToFile(root_url+params, fileName)

# tree = ET.parse(fileName).find("toptracks")

# for item in tree.findall("track"):
    # print(item.find("name").text)

# JSON Output
# json_object = json.loads(raw.read().decode('utf-8'))
# for song in json_object['toptracks']['track']:
	# print(song['name'].encode('utf-8', 'ignore').decode('utf-8', 'ignore'))
