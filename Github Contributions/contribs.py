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


def list_contributions(years):
    """
    List all repositories to which contributions have been made.

    You can then fetch commits off those repos.
    """

    repos = []
    issues = []
    pulls = []

    def process_file(file_):
        with open(file_) as inp:
            soup = BeautifulSoup(inp.read())

        for link in soup.find_all("a", class_="title"):

            url = link.get('href')
            if not url:
                continue

            m = re.match(r'/?(.*?)/(.*?)/commits', url)
            if m:
                repo = (m.group(1), m.group(2))
                if repo not in repos:
                    repos.append(repo)
                continue

            m = re.match(r'/?(.*?)/(.*?)/issues/(\d+)', url)
            if m:
                issue = (m.group(1), m.group(2), m.group(3))
                if issue not in issues:
                    issues.append(issue)
                continue

            m = re.match(r'/?(.*?)/(.*?)/pull/(\d+)', url)
            if m:
                pull = (m.group(1), m.group(2), m.group(3))
                if pull not in pulls:
                    pulls.append(pull)
                continue

            # We should never reach here!
            print()
            print("<|>" + link.parent.text.strip() + "<|>")
            print(url)
            print()

    for year in years:
        for month in range(1, 13):
            process_file(os.path.join(data, str(year), str(month)) + ".htm")

    return repos, issues, pulls

if __name__ == '__main__':
    # fetch_pages(range(2015, 2016))
    r, i, p = list_contributions([2014])

    print(r)
