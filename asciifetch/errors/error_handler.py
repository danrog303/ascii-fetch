import requests
import sys


def error_handler(func_to_wrap):
    def decorator():
        try:
            func_to_wrap()
        except requests.exceptions.ConnectionError:
            print("Connection error. Check your internet connection.", file=sys.stderr)
            exit(1)
    return decorator
