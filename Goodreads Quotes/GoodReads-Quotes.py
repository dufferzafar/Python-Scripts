import urllib.request
import pprint
import sys
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes/list/18654747"

# f = open('/Users/myUserName/Desktop/contacts.html')
# soup = BeautifulSoup(f)
# sys.stdout.errors = 'replace'
# soup = BeautifulSoup(html_doc)
soup = BeautifulSoup(urllib.request.urlopen(url))
list = soup.findAll('div', attrs={'class':'quoteText'})
# print (list)
# pprint.pprint(list)
#

with open("D:\\Output.txt", 'w') as file:
    for item in list:
        file.write("{}\n".format(item))

# print (len(list))
# soup.find_all('a')