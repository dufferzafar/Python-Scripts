import os
import json
import time

import facebook
import requests

from tokens import *

graph = facebook.GraphAPI(USER_TOKEN)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')

count = 1
while True:

    filename = "Data/Posts/%d.json" % count

    # Write JSON to Disk, if it doesn't already exist.
    if not os.path.isfile(filename):

        with open(filename, "w") as out:
            json.dump(posts, out)
            print("Written data to: %s" % filename)

        nxt = posts['paging']['next']
        posts = requests.get(nxt).json()

    else:

        with open(filename) as inp:
            posts = json.load(inp)
            print("Loaded data from: %s" % filename)

    count += 1

    # There are two reasons for an empty response:
    #
    # 1. We got rate limited.
    # 2. This was actually the last post.
    if not posts["data"]:
        for interval in (15, 30, 60, 100):
            posts = requests.get(nxt).json()

            if not posts["data"]:
                print("Got an empty Response. Retrying in %d seconds." % interval)
                time.sleep(interval)
            else:
                break
        else:
            print("The End.")
            break
