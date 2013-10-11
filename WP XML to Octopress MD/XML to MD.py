##################################################
#
# WP XML to Octopress MD
#
# Convert wordpress posts to markdowns.
#
# @dufferzafar
#
##################################################

# Required Libraries
import os
import re
import glob
# import html2text
import xml.etree.ElementTree as ET

# The wordpress namespace dictionary
nsDict = {	'wp': 'http://wordpress.org/export/1.2/',
				'dc': 'http://purl.org/dc/elements/1.1/',
				'content': 'http://purl.org/rss/1.0/modules/content/',
				'excerpt': 'http://wordpress.org/export/1.2/excerpt/'}

# Debugging Output
dbg = open("debug.md", "wb")

# Create output directory, if it doesn't exist
try:
	os.mkdir("Output")
except :
	pass

# Read XML file(s)
for wpXml in glob.glob('*.xml'):
	# print("Reading " + wpXml)
	tree = ET.parse(wpXml).find("channel")

	for item in tree.findall("item"):
		title = item.find("title")
		pName = item.find("wp:post_name", namespaces=nsDict)
		pDate = item.find("wp:post_date", namespaces=nsDict)
		content = item.find("content:encoded", namespaces=nsDict)
		if content.text is not None:
			if pName.text is not None:
				dateTime = re.split("\s", pDate.text)
				# HH:MM Format
				time = re.sub(":\d\d$", "", dateTime[1])
				date = dateTime[0]

				# Output FIle
				fName = date + "-" + pName.text + ".markdown"

				out = open("Output\\" + fName, "w")
				out.write("---\n")
				out.write("layout: post\n")
				out.write('title: "' + title.text + '"\n')
				out.write("date: " + date + " " + time + "\n")
				out.write("comments: false\n")
				out.write("categories:\n")
				out.write("---\n\n")

				out.write(content.text)

print("Done.")