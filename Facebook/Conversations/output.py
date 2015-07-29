"""
Read out the FB Conversation Dumps and Make a nice log file.

You should run messages.py first.
"""

import os
import json
from collections import namedtuple

from config import friends, me

ROOT = "Messages"

Message = namedtuple('Message', ['author', 'body'])

for friend in os.listdir(ROOT):

    messages = {}

    # Read all the files of a friend & build a hashmap
    for file in os.listdir(os.path.join(ROOT, friend)):

        with open(os.path.join(ROOT, friend, file)) as inp:

            data = json.load(inp)
            for act in data['payload']['actions']:

                # BUG: Why wouldn't body be present?
                if 'body' in act:
                    author = act['author'].replace('fbid:', '')

                    if author == me:
                        author = "Me"
                    else:
                        author = friends[author][:4]

                    messages[act['timestamp']] = Message(author, act['body'])

    # Sort by timestamp and iterate
    for stamp in sorted(messages.keys())[:25]:
        m = messages[stamp]
        print('%s:\t%s' % (m.author, m.body))

    print('---------------------------------------------------')
