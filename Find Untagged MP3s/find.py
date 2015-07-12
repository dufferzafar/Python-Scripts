#!/usr/bin/python

import re
import os
import glob
import sys

from mutagen.mp3 import MP3

# Taken from flask_uuid: http://git.io/vmecV
UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

# Musicbrainz Recording ID
# https://picard.musicbrainz.org/docs/mappings/
ufid = u'UFID:http://musicbrainz.org'


def is_tagged(file):
    """ Determine whether an MP3 file is tagged. """
    tags = MP3(file)
    if ufid not in tags:
        return False
    else:
        return re.match(UUID_RE, tags[ufid].data) is not None


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


# Note: Should I just load them in Picard?
def move(files):
    """ Move a list of files to 'Untagged' directory. """
    destination = "Untagged"
    if not os.path.exists(destination):
        os.mkdir(destination)

    for file in files:
        os.rename(file, os.path.join(destination, file))

if __name__ == '__main__':

    # List of files found
    untagged = []

    # Todo: Handle files other than mp3
    for file in glob.glob("*.mp3"):
        if not is_tagged(file):
            print("Found: %s" % file)
            untagged.append(file)

    if confirm("\nMove untagged files?"):
        move(untagged)
