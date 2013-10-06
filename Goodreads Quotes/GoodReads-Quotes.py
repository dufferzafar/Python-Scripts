##################################################
#
# Goodreads Quotes Scraper
#
# Scrapes out all the quotes from GoodReads Quotes
# URL. The results are stored in JSON/XML format.
#
# @dufferzafar
#
##################################################

# Required Libraries
import urllib.request
import os.path
import re

# Output Format
import json

# Make sure you have BeautifulSoup installed
from bs4 import BeautifulSoup

# The URL
url = "https://www.goodreads.com/quotes/list/18654747-shadab-zafar"

# The URL will be saved to this file
fileName = "GRQuotesPage1.html"

# Doownload file only if it does not exist.
if os.path.isfile(fileName):
	print("File Exists. Will Be Read.\n")
else:
	print("File Does Not Exists. Will Be Downloaded.")
	site = urllib.request.urlopen(url)
	data = site.read()

	f = open(fileName, "wb")
	f.write(data)
	f.close()
	print("File Downloaded.")

# Create the soup.
f = open(fileName)
soup = BeautifulSoup(f)
f.close()

# The Debug file
opFile = "debug.txt"

# User Metadata
title = soup.find('title').string.replace("\n", " ")
titleScrape = re.findall('\((.*?)\)', title)

# Username and Total Quotes
user = titleScrape[0]
totalQuotes = re.search('(\d+)$', titleScrape[2]).group(1)

# While Testing and Debugging
# quit()

# Quote text, author name and URL
quoteText = soup.findAll('div', attrs={'class':'quoteText'})

# print (len(quoteText))

# Quote URL
quoteFooterRight = soup.findAll('div', attrs={'class':'right'})

# Begin Scraping
with open(opFile, 'w') as file:
	for (q,r) in zip(quoteText, quoteFooterRight):

		quote = q.contents[0].encode('ascii', 'ignore').decode('ascii', 'ignore')

		qLink = q.find('a')
		authorUrl = qLink.get('href')
		author = qLink.getText()

		rLink = r.find('a')
		quoteUrl = rLink.get('href')

		# json.dumps()

		# print(quoteUrl)
		file.write("Quote = " + re.sub("  +", "", quote.replace("\n", "")) + "\n")
		file.write("QuoteURL = " + quoteUrl + "\n")
		file.write("Author = " + author + "\n")
		file.write("AuthorURL = " + authorUrl + "\n\n\n")
