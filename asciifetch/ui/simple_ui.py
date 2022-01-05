import os
import sys
from urllib.parse import urlparse
from asciifetch.scrapers.scraper_factory import ScraperFactory
from asciifetch.scrapers.art_scraper import ArtScraper
from asciifetch.scrapers.category_scraper import CategoryScraper
from asciifetch.ui.color_print import cprint
from colorama import Style, Fore


class SimpleUI:

    def __init__(self, console_args):
        self.console_args = console_args

    @staticmethod
    def print_category_tree(categories):
        executable_name = os.path.basename(sys.argv[0])
        for category_index, category in enumerate(categories):
            print("{}. {}".format(category_index + 1, f"{category[0]} {category[1]}"))
        print(f"\nRun {Style.BRIGHT}{executable_name} \"https://link-to-the-category\"{Style.RESET_ALL} to select specific category.")

    @staticmethod
    def print_images(images, color, bold, number=-1):
        executable_name = os.path.basename(sys.argv[0])
        color_code = getattr(Fore, color.upper())
        if number == -1:
            cprint("Printing all ASCII arts in specified category", bold=True)
            for index, ascii_art in enumerate(images):
                print(f"----------#{index}----------")
                cprint(ascii_art + "\n", color=color_code, bold=bold)
            print(f"\nRun {Style.BRIGHT}{executable_name} \"https://link-to-the-category\" N{Style.RESET_ALL} to print only N-th image.")
        else:
            cprint(images[number] + "\n", color=color_code, bold=bold)

    def print_ui(self):
        requested_path = list(self.console_args.requested_path)

        if len(requested_path) > 0 and urlparse(requested_path[0]).netloc not in ["asciiart.eu", "www.asciiart.eu"]:
            print(f"{requested_path[0]} isn't a asciiart.eu URL link!", file=sys.stderr)
            print("Please check --help for usage manual.", file=sys.stderr)
            exit(3)

        if len(requested_path) == 0:
            cprint("Printing top level categories:", bold=True)
            main_categories = ScraperFactory("https://asciiart.eu/").get_scraper().get_categories()
            self.print_category_tree(main_categories)
        elif len(requested_path) == 1:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            if isinstance(scraper, ArtScraper):
                self.print_images(scraper.get_ascii_arts(), self.console_args.color, self.console_args.bold)
            elif isinstance(scraper, CategoryScraper):
                cprint("Printing available categories:", bold=True)
                cats = scraper.get_categories()
                self.print_category_tree(cats)
            elif scraper is None:
                print("(no data detected - are you sure you passed correct link?")
        elif len(requested_path) == 2:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            if scraper is ArtScraper:
                requested_index = int(requested_path[1])
                self.print_images(scraper.get_ascii_arts(), self.console_args.color, self.console_args.bold, requested_index)
            else:
                print("(no data detected - are you sure you passed correct asciiart.eu link?", file=sys.stderr)
        else:
            print("Unrecognized amount of arguments.", file=sys.stderr)
            print("Please check --help for usage manual.", file=sys.stderr)
            exit(4)
