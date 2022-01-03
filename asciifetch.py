from asciifetch.scrapers.category_scraper import CategoryScraper
from asciifetch.scrapers.art_scraper import ArtScraper


def main():
    # Example 1
    # Printing ASCII Art number 2 from https://www.asciiart.eu/animals/deer
    print(ArtScraper("https://www.asciiart.eu/animals/deer").get_ascii_arts()[1])

    # Example 2
    # Printing all subcategories in https://www.asciiart.eu/animals
    print(CategoryScraper("https://www.asciiart.eu/animals").get_categories())


if __name__ == '__main__':
    main()