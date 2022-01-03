import requests
from bs4 import BeautifulSoup
from asciifetch.scrapers.category_scraper import CategoryScraper
from asciifetch.scrapers.art_scraper import ArtScraper


class ScraperFactory:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).text, "html.parser")

    def get_scraper(self):
        if len(self.soup.select(".asciiarts pre[class]")) == 0:
            return CategoryScraper(self.soup)
        else:
            return ArtScraper(self.soup)
