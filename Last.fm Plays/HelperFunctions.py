import os
import urllib.request

def downloadToFile(url, fileName):
    """
    Download a url to file.

    Does nothing if the file already exist
    """

    # Check if the file exist?
    if not os.path.isfile(fileName):

        try:
            site = urllib.request.urlopen(url)
            data = site.read()

            f = open(fileName, "wb")
            f.write(data)
            f.close()
            # print("File Downloaded.")
            return 1

        except:
            return 0
