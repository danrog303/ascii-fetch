#!/usr/bin/env python3
import asciifetch.ui.keyboard_interrupt_handle
from asciifetch.ui.simple_ui import SimpleUI
from asciifetch.ui.error_handler import error_handler
import argparse


@error_handler
def main():
    parser = argparse.ArgumentParser(
        description="Downloads and displays ASCII images in your terminal.",
        epilog="https://github.com/danrog303/ascii-fetch"
    )
    parser.add_argument(nargs='*', dest="requested_path")
    parser.add_argument(
        "--color", dest="color", metavar="color_name",
        help="Color of displayed ascii arts",
        choices=['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'white', 'yellow'],
        default="reset"
    )
    parser.add_argument(
        "--bold", dest="bold",
        help="Should ascii art be bolded?",
        action="store_true", default=False
    )
    args = parser.parse_args()
    SimpleUI(args).print_ui()


if __name__ == '__main__':
    main()
