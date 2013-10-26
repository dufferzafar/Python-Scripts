from datetime import datetime as DT
from datetime import timedelta
import xml.etree.ElementTree as ET

# Current File
# todo: Rename the files present in Backups Folder
fileName = "Backups/Dec-2012.xml"

# Build a parse tree
tree = ET.parse(fileName).find("dialup")

# Per Day
timePerDay = [0 for i in range(1, 33)]

downloadPerDay = [0 for i in range(1, 33)]
uploadPerDay = [0 for i in range(1, 33)]

# Rock This Show!!
for item in tree.findall("item"):
    conName = item.find("connection").text
    if conName != "MBlaze USB Modem":
        continue

    dur = item.find("duration").text
    since = item.find("since").text
    downloaded = item.find("in").text
    uploaded = item.find("out").text

    sessStart = DT.strptime(since, "%Y-%m-%d %H:%M:%S")
    # sessDuration = timedelta(seconds=int(dur))

    timePerDay[sessStart.date().day] += int(dur)
    downloadPerDay[sessStart.date().day] += int(downloaded)
    uploadPerDay[sessStart.date().day] += int(uploaded)

# Build Output Graphing Lists
labelValues = [0 for i in range(1, 33)]
outValues = [[],[],[]]
outValues[0] = [0 for i in range(1, 33)]
outValues[1] = [0 for i in range(1, 33)]
outValues[2] = [0 for i in range(1, 33)]

# Time Spent Per Day on the Internet
for i in range(1,32):
    labelValues[i] = i
    outValues[0][i] = downloadPerDay[i]//(1024*1024)
    outValues[1][i] = uploadPerDay[i]//(1024*1024)
    outValues[2][i] = timePerDay[i]//60
    print(str(i) + " " + str(timedelta(seconds=timePerDay[i])))

# Write Output to fileself.
opFile = open("Output\dataset.js", "w")
opFile.write("var labelValues = " + str(labelValues))
opFile.write("\nvar downloadPerDay = " + str(outValues[0]))
opFile.write("\nvar uploadPerDay = " + str(outValues[1]))
opFile.write("\nvar timePerDay = " + str(outValues[2]))
opFile.close()