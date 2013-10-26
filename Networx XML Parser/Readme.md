# Networx XML Parser v0.2

Parse [Networx](http://www.softperfect.com/products/networx) backup XMLs to create statistics on Internet Usage.


## Table of Contents

* [Usage Scenario](#usage)
* [Stuff to do](#todo)
* [Changelog](#changelog)

## <a name="usage"></a>Usage Scenario

I've been creating a backup of Networx Data every month for the past one year. The backups are saved in XML format.

I now wish to use all that data to create some usage statistics.

These set of scripts will parse those XML Files to convert the crude data into a more usable format.

I'll proabably be creating js files so that the data can be charted using some graphing library.

## <a name="todo"></a>Todo

* Better Graphing Ideas

* Time Per Day
  * Matrix[Month][Day]

* Sessions Per Day
  * Started At
  * Duration
  * Ended At

* Connection Wise

## <a name="changelog"></a>Changelog

* December Graph Done :)
* Time Per Day for December

* Testing/Learning
  * List = [0] * 10
  * Datetime Module: strptime, timedelta