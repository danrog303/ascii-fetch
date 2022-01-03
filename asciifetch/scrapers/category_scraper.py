import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin


class CategoryScraper:

    @staticmethod
    def make_link_absolute(href):
        return urljoin("https://asciiart.eu", href)

    def __init__(self, url):
        self.url = url
        self.html_doc = requests.get(url).text
        self.soup = BeautifulSoup(self.html_doc, "html.parser")

    def is_top_level(self):
        category_path = urlsplit(self.url).path
        return category_path == "" or category_path == "/"

    def get_categories(self):
        category_tags = self.soup.select("#directory .directory-columns a")
        if self.is_top_level():
            categories = [(self.make_link_absolute(a["href"]), a.text) for a in category_tags]
        else:
            categories = [(self.make_link_absolute(a["href"]), a.text[:-1])
                          for a in category_tags if a.text.endswith("@")]
        return categories

    def get_arts(self):
        if self.is_top_level():
            return []
        else:
            a_tags = self.soup.select("#directory .directory-columns a")
            arts = [(self.make_link_absolute(a["href"]), a.text) for a in a_tags if not a.text.endswith("@")]
            return arts
