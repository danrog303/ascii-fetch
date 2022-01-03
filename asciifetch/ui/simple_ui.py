import os
import sys
from asciifetch.scrapers.scraper_factory import ScraperFactory
from asciifetch.scrapers.art_scraper import ArtScraper
from asciifetch.scrapers.category_scraper import CategoryScraper


class SimpleUI:

    def __init__(self, console_args):
        self.console_args = console_args

    @staticmethod
    def print_category_tree(categories):
        executable_name = os.path.basename(sys.argv[0])
        for category_index, category in enumerate(categories):
            print("{}. {}".format(category_index + 1, f"{category[0]} {category[1]}"))
        print(f"\nRun {executable_name} \"https://link-to-the-category\" to select specific category.")

    @staticmethod
    def print_images(images, number=-1):
        executable_name = os.path.basename(sys.argv[0])
        if number == -1:
            print("Printing all ASCII arts in specified category")
            for index, ascii_art in enumerate(images):
                print(f"----------#{index}----------")
                print(ascii_art + "\n")
            print(f"\nRun {executable_name} \"https://link-to-the-category\" N to print only N-th image.")

    def print_ui(self):
        requested_path = list(self.console_args.requested_path)

        if len(requested_path) == 0:
            print("Printing top level categories:")
            main_categories = ScraperFactory("https://asciiart.eu/").get_scraper().get_categories()
            self.print_category_tree(main_categories)
        elif len(requested_path) == 1:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            if isinstance(scraper, ArtScraper):
                self.print_images(scraper.get_ascii_arts())
            elif isinstance(scraper, CategoryScraper):
                print("Printing subcategories:")
                self.print_category_tree(scraper.get_categories())
        elif len(requested_path) == 2:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            requested_index = int(requested_path[1])
            image = scraper.get_ascii_arts()[requested_index]
            print(image)
