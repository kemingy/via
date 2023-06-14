import argparse

from via.ignore import download_ignore_file
from via.license import download_license


def main():
    parser = argparse.ArgumentParser(description="via args parser")
    parser.add_argument("-i", "--ignore", help="ignore language")
    parser.add_argument("-l", "--license", help="license name")
    parser.add_argument("-p", "--print", help="print to stdout", action="store_true")
    args = parser.parse_args()

    if args.ignore:
        download_ignore_file(args.ignore, args.print)

    if args.license:
        download_license(args.license, args.print)

    if not (args.ignore or args.license):
        print(parser.print_help())
