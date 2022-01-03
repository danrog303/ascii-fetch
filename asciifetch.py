import argparse
from asciifetch.ui.simple_ui import SimpleUI


def main():
    parser = argparse.ArgumentParser(
        description="Downloads and displays ASCII images in your terminal.",
        epilog="https://github.com/danrog303/ascii-fetch"
    )
    parser.add_argument(nargs='*', dest="requested_path")
    args = parser.parse_args()
    SimpleUI(args).print_ui()


if __name__ == '__main__':
    main()
