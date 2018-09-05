import argparse

from .ignore import download_file
from .license import download_license

def main():
    parser = argparse.ArgumentParser(description='via args parser')
    parser.add_argument('-i', '--ignore', help='ignore language')
    parser.add_argument('-l', '--license', help='license name')
    args = parser.parse_args()

    if args.ignore:
        download_file(args.ignore)

    if args.license:
        download_license(args.license)

    if not (args.ignore or args.license):
        print(parser.print_help())