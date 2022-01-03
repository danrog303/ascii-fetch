class ArtScraper:

    def __init__(self, soup):
        self.soup = soup

    def get_ascii_arts(self):
        art_tags = self.soup.select(".asciiarts pre[class]")
        return [art.text for art in art_tags]
