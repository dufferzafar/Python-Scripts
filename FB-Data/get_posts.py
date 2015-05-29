import json

import facebook
import requests

from tokens import *

graph = facebook.GraphAPI(USER_TOKEN)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')

count = 1
while True:

    # Write JSON to Disk
    filename = "Data/Posts/%d.json" % count
    with open(filename, "w") as out:
        json.dump(posts, out)
        print("Written data to: %s" % filename)

    count += 1

    try:
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        print("The End.")
        break
