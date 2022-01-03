import os
from colorama import Fore, Style, init as color_conversion_init


_color_conversion_enabled = False
if not _color_conversion_enabled and os.name == "nt":
    color_conversion_init(convert=True)
    _color_conversion_enabled = True


def cprint(*args, color=None, bold=False):
    if bold:
        print(f"{Style.BRIGHT}", end="")
    if color:
        print(f"{color}", end="")
    print(*args, end="")
    print(f"{Style.RESET_ALL}")
