import requests
from bs4 import BeautifulSoup

class scraper:
    def __init__(self, url) -> None:
        self.url = url
        # spoof to make it think it is coming from firefox on linux
        self.headers = {'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'GET',
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Max-Age': '3600',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def getUrlPage(self):
        # POST to url and GET the response
        _pageAsHtml = requests.get(self.url, self.headers)
        return _pageAsHtml.content

    def findInContent(self):
        # need to put a input to find tag
        # pass getUrlPage and parser
        # loop through conent line by line print matches
        pageSoup = BeautifulSoup(self.getUrlPage(), "html.parser")
        for _a in pageSoup.find_all("a"):
            print(f"found url: {_a}")


if __name__ == "__main__":
    _obj = scraper("http://archive.ics.uci.edu/ml/datasets/auto+mpg")
    _obj.getUrlPage()
    _obj.findInContent()