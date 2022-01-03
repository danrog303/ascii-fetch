import argparse
from asciifetch.scrapers.category_scraper import CategoryScraper
from asciifetch.scrapers.art_scraper import ArtScraper


def main():
    parser = argparse.ArgumentParser(
        description="Downloads and displays ASCII images in your terminal.",
        epilog="https://github.com/danrog303/ascii-fetch"
    )
    parser.add_argument(nargs='*', dest="requested_path")
    args = parser.parse_args()


if __name__ == '__main__':
    main()