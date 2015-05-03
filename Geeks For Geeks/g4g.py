import sys
import requests

from bs4 import BeautifulSoup
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication


def parse(url):
    """ Fetch a URL and return post content. """

    # Soupify!
    response = requests.get(url)

    if not response.ok:
        return ''

    soup = BeautifulSoup(response.text)

    # Remove big stuff!
    for elem in soup.findAll(['script', 'style', 'ins', 'iframe']):
        elem.extract()

    for elem in soup.select('div.comments-main'):
        elem.extract()

    content = soup.find(id="content")
    html = content.decode_contents()

    # Details, baby!
    block = ['div', 'Related Topics', 'twitter-share-button', 'g:plusone',
             'Please write comments']

    lines = html.splitlines(True)

    for line in lines:
        for item in block:
            if item in line:
                lines.remove(line)
                break

    html = ''.join(lines)
    return html


def print_pdf(html, filename):
    """ Print HTML to PDF. """

    doc = QTextDocument()
    doc.setHtml(html)

    printer = QPrinter()
    printer.setOutputFileName(filename)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setPageSize(QPrinter.A4)
    printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)

    doc.print_(printer)

    print("PDF Generated: " + filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    from links import topic_sets

    for topic in topic_sets:
        print("Working on: " + topic[0])

        html = ""

        # Fetch each set
        for num in range(1, topic[2] + 1):
            html += parse(topic[1] % num)

        print_pdf(html, topic[0] + ".pdf")

    QApplication.exit()
