import os
import HelperFunctions as HF

usrRoot = "http://chatlogs.musicbrainz.org/musicbrainz"
devRoot = "http://chatlogs.musicbrainz.org/musicbrainz-devel"

year = "2015"

for m in range(1, 7):
    for d in range(1, 32):

        mon = "0" + str(m) if m < 10 else str(m)
        day = "0" + str(d) if d < 10 else str(d)

        try:
            os.mkdir("Devel/" + mon)
        except:
            pass

        try:
            os.mkdir("Usr/" + mon)
        except:
            pass

        fileName = mon + "/" + year + "-" + mon + "-" + day + ".txt"

        devUrl = devRoot + "/" + year + "/" + year + "-" + fileName
        usrUrl = usrRoot + "/" + year + "/" + year + "-" + fileName

        print("Dnld Devel... " + fileName)
        HF.downloadToFile(devUrl, "Devel/" + fileName)
        print("Dnld User... " + "Usr/" + fileName)
        HF.downloadToFile(usrUrl, "Usr/" + fileName)

    print("=======================================")


# Phew!!
print("All Done!")
