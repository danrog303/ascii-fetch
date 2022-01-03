import os
import sys
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

        if len(requested_path) == 0:
            cprint("Printing top level categories:", bold=True)
            main_categories = ScraperFactory("https://asciiart.eu/").get_scraper().get_categories()
            self.print_category_tree(main_categories)
        elif len(requested_path) == 1:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            if isinstance(scraper, ArtScraper):
                self.print_images(scraper.get_ascii_arts(), self.console_args.color, self.console_args.bold)
            elif isinstance(scraper, CategoryScraper):
                cprint("Printing subcategories:", bold=True)
                self.print_category_tree(scraper.get_categories())
        elif len(requested_path) == 2:
            scraper = ScraperFactory(requested_path[0]).get_scraper()
            requested_index = int(requested_path[1])
            self.print_images(scraper.get_ascii_arts(), self.console_args.color, self.console_args.bold, requested_index)