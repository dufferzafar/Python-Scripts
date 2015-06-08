import os
import re
import requests

from bs4 import BeautifulSoup


data = "Data"
user = "dufferzafar"
github = "https://github.com"


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

            if '/commits' in url:
                if url not in repos:
                    repos.append(url)

            # Bug: Github website has endpoint 'pull'
            # while the API has 'pulls'. WUT!
            elif '/pull' in url:
                if url not in pulls:
                    pulls.append(url)

            elif '/issues' in url:
                if url not in issues:
                    issues.append(url)

            else:
                # Let's hope we never reach here!
                print(url)

    for year in years:
        for month in range(1, 13):
            process_file(os.path.join(data, str(year), str(month)) + ".htm")

    return repos, issues, pulls

if __name__ == '__main__':
    # fetch_pages(range(2015, 2016))
    rpo, iss, pll = list_contributions([2012, 2013])

    # Worked on repos
    for r in sorted(rpo):
        print(github + r)

    print("\n")

    # Issues reported
    for i in sorted(iss):
        print(github + i)

    print("\n")

    # Pulls created
    for p in sorted(pll):
        print(github + p)
