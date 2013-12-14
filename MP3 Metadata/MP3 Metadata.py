import os
import re

# Python 3 port of Mutagen 3 : https://github.com/LordSputnik/mutagen
# from mutagenx.mp3 import MP3
from mutagenx.id3 import ID3, TOPE, TPE1

directory = "G:\\Music\\Coke Studio\\Papon\\"

for dirpath, dirnames, files in os.walk(directory):
   for filename in files:
      if filename.endswith('mp3'):
         print(filename)
         tags = ID3(os.path.join(dirpath, filename))

         # tags["TOPE"] = TOPE(encoding=0, text=re.sub('(\s?)[&,]', ' /', str(tags["TOPE"])))
         tags["TPE1"] = TPE1(encoding=0, text=re.sub('(\s?)[&,]', ' /', str(tags["TPE1"])))
         tags.save()

         # print(tags["TPE1"])
         # print(tags.pprint())



