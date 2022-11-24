from uiuc_apartments import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--agencies", nargs='+', help="Agencies to run")
    args = parser.parse_args()
    agencies = set([] if args.agencies is None else args.agencies)

    for agency in AllAgencies:
        if len(agencies) == 0 or agency.name in agencies:
            retrieved = agency.get_all()
            print(retrieved[:10])
            print()