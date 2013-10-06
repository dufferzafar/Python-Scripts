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

# Make sure you have BeautifulSoup installed
from bs4 import BeautifulSoup

# The URL
url = "https://www.goodreads.com/quotes/list/18654747"

# The URL will be saved to this file
fileName = "GRQuotesPage1.html"

# Doownload file only if it does not exist.
if os.path.isfile(fileName):
	print("File Exists. Will Be Read.")
else:
	print("File Does Not Exists. Will Be Downloaded.")
	site = urllib.request.urlopen(url)
	data = site.read()

	f = open(fileName, "wb")
	f.write(data)
	f.close()

# Create the soup.
f = open(fileName)
soup = BeautifulSoup(f)
f.close()

# The Debug file
opFile = "debug.html"

# Quote text and author URL
quoteText = soup.findAll('div', attrs={'class':'quoteText'})

# Begin Scraping
with open(opFile, 'wb') as file:
	for item in quoteText:
		quote = item.contents[0].encode('ascii', 'ignore')

		# link = item.find('a')
		# authorUrl = link.get('href')
		# author = link.getText

		print(quote)
		# file.write(command)

# print (len(quoteText))