import os
import urllib.request

def downloadToFile(url, fn):
    """
    Download a url to file.

    Does nothing if the file already exist
    """

    # Check if the file exist?
    if not os.path.isfile(fn):

        try:
            site = urllib.request.urlopen(url)
            data = site.read()

            f = open(fn, "wb")
            f.write(data)
            f.close()
            # print("File Downloaded.")
            return 1

        except:
            return 0
