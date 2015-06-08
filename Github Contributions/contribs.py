import os
import re
import requests

from bs4 import BeautifulSoup


data = "Data"
user = "dufferzafar"


def fetch_pages(years):
    """Fetch contribution pages from github and store them as html files."""

    def process_url(url, out):
        """Download a page and extract out the contributions."""

        print("%s\t====>\t%s" % (url, out))

        response = requests.get(url)

        soup = BeautifulSoup(response.text)
        contribs = soup.find_all('div', class_="contribution-activity-listing")[0]
        html = contribs.decode_contents()

        with open(out, "w") as out:
            out.write(html)

    gh_url = ("https://github.com/%s?tab=contributions"
              "&from=%d-%d-01&to=%d-%d-01")

    for year in years:

        # Create the destination folder
        folder = os.path.join(data, str(year))
        if not os.path.exists(folder):
            os.makedirs(folder)

        for month in range(1, 13):
            out = os.path.join(folder, str(month) + ".htm")

            if month == 12:
                params = (user, year, month, year+1, 1)
            else:
                params = (user, year, month, year, month+1)

            process_url(gh_url % params, out)
