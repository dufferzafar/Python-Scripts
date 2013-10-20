import os
import urllib.request

def downloadToFile(url, fileName):
    """
    Download a url to file.

    Does nothing if the file already exist
    """

    # Check if the file exist?
    if os.path.isfile(fileName):
        # print("File Exists. Will Be Read.\n")
        pass
    else:
        # print("File Does Not Exists. Will Be Downloaded.")
        site = urllib.request.urlopen(url)
        data = site.read()

        f = open(fileName, "wb")
        f.write(data)
        f.close()
        # print("File Downloaded.")
