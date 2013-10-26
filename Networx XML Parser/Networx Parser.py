from datetime import datetime as DT
from datetime import timedelta
import xml.etree.ElementTree as ET

sessStart = DT.strptime("2012-12-01 14:10:31", "%Y-%m-%d %H:%M:%S")
sessDuration = timedelta(seconds=int("4692"))

# print(sessStart.date().day, sessStart.time())
# print(sessStart.time(), (sessStart + sessDuration).time())

l = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(l[87])