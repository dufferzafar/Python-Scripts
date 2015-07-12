#!/usr/bin/python

import re
import os
import glob
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



# Untagged files will be moved
# Note: Should I just load them in Picard?
destination = "Untagged"
if not os.path.exists(destination):
    os.mkdir(destination)

if __name__ == '__main__':

    # Todo: Handle files other than mp3
    for file in glob.glob("*.mp3"):

        if not is_tagged(file):
            print("Moving: %s" % file)
