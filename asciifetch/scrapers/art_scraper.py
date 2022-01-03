import requests
from bs4 import BeautifulSoup


class ArtScraper:

    def __init__(self, url):
        self.url = url
        self.html_doc = requests.get(url).text
        self.soup = BeautifulSoup(self.html_doc, "html.parser")

    def get_ascii_arts(self):
        art_tags = self.soup.select(".asciiarts pre[class]")
        return [art.text for art in art_tags]

