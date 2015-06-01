import os
import urllib.request


def process_url(url, out):

    site = urllib.request.urlopen(gh_url % params)

    with open(out, "wb") as out:
        out.write(site.read())

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
            print("Fetching: " + out)

            if month == 12:
                params = (year, month, year+1, 1)
            else:
                params = (year, month, year, month+1)

            process_url(gh_url % params, out)
