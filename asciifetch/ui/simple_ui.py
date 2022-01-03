import os
import sys
from asciifetch.scrapers.category_scraper import CategoryScraper
from asciifetch.scrapers.art_scraper import ArtScraper


class SimpleUI:

    def __init__(self, console_args):
        self.console_args = console_args

    def print_ui(self):
        requested_path = self.console_args.requested_path
        executable_name = os.path.basename(sys.argv[0])

        if len(requested_path) == 0:
            print("Printing top level categories:")
            categories = CategoryScraper("https://asciiart.eu/").get_categories()
            for category_number, category in enumerate(categories):
                print(f"[{category_number + 1}] {category[1]}")
            print(f"\nRun {executable_name} 1 or {executable_name} \"{categories[0][1]}\" to select specific category.")
