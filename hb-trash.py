import csv
import os

import requests
import argparse
import pandas as pd


def init_argparse():
    parser = argparse.ArgumentParser(
        description="Tool for getting the garbage collection dates in Bremen, Germany as ics or csv")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("-i", "--ical", action="store_true", help="ical format")
    action.add_argument("-c", "--csv", action="store_true", help="csv format")
    # force to get an integer as value
    parser.add_argument("-s", "--street", type=str, help="Name of street", required=True)
    parser.add_argument("-n", "--nr", type=str, help="Street number", required=True)
    parser.add_argument("-d", "--dashboard", action="store_true")
    return parser.parse_args()


def get_data(format, args):
    r = requests.post(
        "https://web.c-trace.de/bremenabfallkalender/(S(bipsbtlhddavyhhnypfj2wwp))/abfallkalender/{}?abfall=".format(
            format), params={"strasse": str(args.street), "hausnr": str(args.nr)})
    csv_string = r.content.decode("ISO-8859-1")
    with open("hb-trash.{}".format("ics" if format == "cal" else format), "w") as file:
        file.write(csv_string)


def writeNextPickup():
    if os.path.exists("hb-trash.csv"):
        df = pd.read_csv("hb-trash.csv")
        tmp = df.to_json()
        print(tmp)
        with open("hb-trash.csv", "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                print(list(line))
    else:
        raise FileNotFoundError


def check_args(args):
    if args.ical:
        get_data("cal", args)
    elif args.csv:
        get_data("csv", args)
    else:
        raise Exception()
    if args.dashboard:
        writeNextPickup()


if __name__ == '__main__':
    check_args(init_argparse())
