"""
TED talk Renamer.

'JamesGeary_2009G-480p.mp4' becomes 'James Geary - Metaphorically speaking.mp4'
"""

import re
import os

from ted_talks_list import talks

from fuzzywuzzy import process

ted_folder = os.path.expanduser("~/Videos/TED/")

if __name__ == '__main__':

    for file in os.listdir(ted_folder):

        name, ext = os.path.splitext(file)
        name = name.replace("-480p", "")
        name = re.sub(r"_\d{4}P", "", name)  # Remove year '_2014P'

        talk = process.extractOne(name, talks, score_cutoff=50)
        if talk:
            newfile = "%s%s" % (talk[0], ext)

            os.rename(
                os.path.join(ted_folder, file),
                os.path.join(ted_folder, newfile)
            )

            print("Convert: '%s' --> '%s' [%d]" %
                  (file, newfile, talk[1]))
        else:
            print("Skipping: %s" % file)
