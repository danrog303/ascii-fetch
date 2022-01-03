from urllib.parse import urlsplit, urljoin


class CategoryScraper:

    @staticmethod
    def make_link_absolute(href):
        return urljoin("https://asciiart.eu", href)

    def __init__(self, soup):
        self.soup = soup

    def get_categories(self):
        category_tags = self.soup.select("#directory .directory-columns a")
        categories = [(a.text, self.make_link_absolute(a["href"])) for a in category_tags]
        return categories
