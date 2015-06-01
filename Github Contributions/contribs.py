import os
import requests

from bs4 import BeautifulSoup


def process_url(url, out):
    print("%s\t====>\t%s" % (url, out))

    response = requests.get(url)

    soup = BeautifulSoup(response.text)
    contribs = soup.find_all('div', class_="contribution-activity-listing")[0]
    html = contribs.decode_contents()

    with open(out, "w") as out:
        out.write(html)

if __name__ == '__main__':

    gh_url = "https://github.com/dufferzafar" \
        "?tab=contributions&from=%d-%d-01&to=%d-%d-01"

    data = "Data"

    for year in range(2012, 2016):

        # Create the destination folder
        folder = os.path.join(data, str(year))
        if not os.path.exists(folder):
            os.makedirs(folder)

        for month in range(1, 13):
            out = os.path.join(folder, str(month) + ".htm")

            if month == 12:
                params = (year, month, year+1, 1)
            else:
                params = (year, month, year, month+1)

            process_url(gh_url % params, out)
