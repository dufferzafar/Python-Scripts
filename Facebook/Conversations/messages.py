"""
Backup your entire facebook conversations.

Friend list is read from a config file.
"""

import json
import os
import requests
import sys
import time

from config import friends, form_data, headers


# Can be used to download a range of messages
limit = 2000

# Used to find the end of conversation thread
END_MARK = "end_of_history"

FB_URL = "https://www.facebook.com/ajax/mercury/thread_info.php"

ROOT = "Messages"


def mkdir(f):
    """ Create a directory if it doesn't already exist. """
    if not os.path.exists(f):
        os.makedirs(f)


def fetch(data):
    """ Fetch data from Facebook. """

    offset = [v for k, v in data.items() if 'offset' in k][0]
    limit = [v for k, v in data.items() if 'limit' in k][0]

    print("\t%6d  -  %6d" % (offset, offset+limit))

    response = requests.post(FB_URL, data=data, headers=headers)

    # Account for 'for (;;);' in the beginning of the text.
    return response.content[9:]


def confirm(question):
    """ Confirm whether the files should be moved. """
    valid = {'y': True, 'n': False}
    while True:
        sys.stdout.write(question + " [y/n]: ")
        choice = raw_input().lower()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'y' or 'n'.\n")


if __name__ == '__main__':

    for friend_id, friend_name in friends.items():

        if not confirm("Fetch converstaion with '%s'?" % friend_name):
            continue

        print("Retrieving Messages of: %s" % friend_name)

        # Setup data directory
        dirname = os.path.join(ROOT, friend_name)
        mkdir(dirname)

        # These parameters need to be reset everytime
        offset = 0
        timestamp = 0
        data = {"payload": ""}

        # We want it ALL!
        while END_MARK not in data['payload']:

            form_data["messages[user_ids][%s][offset]" % friend_id] = offset
            form_data["messages[user_ids][%s][limit]" % friend_id] = limit
            form_data["messages[user_ids][%s][timestamp]" % friend_id] = str(timestamp)

            content = fetch(form_data)

            # Handle facebook rate limits
            while not content:
                print("Facebook Rate Limit Reached. Retrying after 30 secs")
                time.sleep(30)
                content = fetch(form_data)

            # Build JSON representation
            data = json.loads(content)

            # Dump Data
            filename = "%s.json" % (limit+offset)
            with open(os.path.join(dirname, filename), "w") as op:
                json.dump(data, op, indent=2)

            # Next!
            offset = offset + limit
            timestamp = data['payload']['actions'][0]['timestamp']
            time.sleep(2)

        # Make the form_data usable for the next user
        form_data.pop("messages[user_ids][%s][offset]" % friend_id)
        form_data.pop("messages[user_ids][%s][limit]" % friend_id)

        print("\t-----END-----")
