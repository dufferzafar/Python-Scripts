import os
import glob
from mutagen.mp3 import MP3

# Musicbrainz Tags
mb_tags = [
    u'TXXX:MusicBrainz Artist Id',
    u'TXXX:MusicBrainz Release Group Id',
    u'TXXX:MusicBrainz Album Id',
    # u'TXXX:MusicBrainz Album Artist Id',
    # u'TXXX:MusicBrainz Release Track Id',
    # u'TXXX:MusicBrainz Album Status',
    # u'TXXX:MusicBrainz Album Type',
]


def is_tagged(file):
    """
    Determine whether an MP3 file is tagged.

    Todo:
        What if a file has the tags, but their 'value' is wrong?
        So we need to ensure that the Ids are actually UUIDs.

        Handle [non-album-tracks] which only have an Artist ID.
    """
    # See if all these tags exist in the file
    for tag in mb_tags:
        if tag not in MP3(file):
            return False, tag
    return True, None

# Untagged files will be moved
# Note: Should I just load them in Picard?
destination = "Untagged"
if not os.path.exists(destination):
    os.mkdir(destination)

if __name__ == '__main__':

    # Todo: Handle files other than mp3
    for file in glob.glob("*.mp3"):

        tagged, tag = is_tagged(file)

        if not tagged:
            print("%s not found in %s" % (tag, file))
            os.rename(file, os.path.join(destination, file))
