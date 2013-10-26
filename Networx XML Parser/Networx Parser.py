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

# Rock This Show!!
for item in tree.findall("item"):
    conName = item.find("connection").text
    if conName != "MBlaze USB Modem":
        continue

    dur = item.find("duration").text
    since = item.find("since").text

    sessStart = DT.strptime(since, "%Y-%m-%d %H:%M:%S")
    # sessDuration = timedelta(seconds=int(dur))

    timePerDay[sessStart.date().day] += int(dur)

# Build Output Graphing Lists
labelValues = [0 for i in range(1, 33)]
dataValues = [0 for i in range(1, 33)]

# Time Spent Per Day on the Internet
for i in range(1,32):
    labelValues[i] = i
    dataValues[i] = timePerDay[i]//60

    print(str(i) + " " + str(timedelta(seconds=timePerDay[i])))

# Write Output to fileself.
opFile = open("Output\dataset.js", "w")
opFile.write("var labelValues = " + str(labelValues))
opFile.write("\nvar dataValues = " + str(dataValues))
opFile.close()