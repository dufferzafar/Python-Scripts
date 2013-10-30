from datetime import datetime as DT
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# from datetime import timedelta
# http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&user=dufferzafar&from=1383004800&api_key=da70281f2f464cfaa4638c4bfe820f9a
# http://ws.audioscrobbler.com/2.0/?method=user.getInfo&user=dufferzafar&api_key=da70281f2f464cfaa4638c4bfe820f9a
# http://ws.audioscrobbler.com/2.0/?method=user.getFriends&user=dufferzafar&recenttracks=0&api_key=da70281f2f464cfaa4638c4bfe820f9a

# The timestamp of today
unixTSToday = int(time.mktime(time.strptime(DT.strftime(DT.today(), '%Y-%m-%d'), '%Y-%m-%d'))) - time.timezone

# Don't abuse, Please.
api_key = "da70281f2f464cfaa4638c4bfe820f9a"

# Last.fm API
root_url = "http://ws.audioscrobbler.com/2.0/?"
params = urllib.parse.urlencode({'method': 'user.getRecentTracks', 'user': 'dufferzafar', 'from': unixTSToday, 'api_key': api_key})
params2 = urllib.parse.urlencode({'method': 'user.getRecentTracks', 'user': 'shivamrana', 'from': unixTSToday, 'api_key': api_key})
# The file where lastfm response will be saved
# print("Downloading Data...")

site = urllib.request.urlopen(root_url+params)
site2 = urllib.request.urlopen(root_url+params2)

# Build a parse tree
node = ET.fromstring(site.read()).find("recenttracks")
node2 = ET.fromstring(site2.read()).find("recenttracks")
print("Shadab = " + node.attrib['total'])
print("Shivam = " + node2.attrib['total'])