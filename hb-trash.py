import argparse
import csv
import datetime
import json

import requests


def init_argparse():
    parser = argparse.ArgumentParser(
        description="Tool for getting the garbage collection dates in Bremen, Germany as ics or csv")
    # force to get an integer as value
    parser.add_argument("-s", "--street", type=str, help="Name of street", required=True)
    parser.add_argument("-n", "--nr", type=str, help="Street number", required=True)
    parser.add_argument("-d", "--dashboard", action="store_true")
    return parser.parse_args()
def write(content):
    print(str(content))
    with open('nextpickup.json', "w") as file:
        json.dump(content,file)

def get_data(args):
    r = requests.post(
        "https://web.c-trace.de/bremenabfallkalender/(S(bipsbtlhddavyhhnypfj2wwp))/abfallkalender/csv?abfall=",
        params={"strasse": str(args.street), "hausnr": str(args.nr)})
    csv_string = r.content.decode("ISO-8859-1")
    lines = csv_string.splitlines()
    content = list(csv.reader(lines))
    now = datetime.datetime.now()
    for line in content[1:]:
        date = datetime.datetime.strptime(line[0].split('"')[1], "%d.%m.%Y")
        if (date - now).days > -1:
            break
    if line[0].split('"')[3] != "Papier / Gelber Sack":
        write({"date": date.strftime("%d.%m.%Y"), "type": 1, "lastupdate": now.strftime("%d.%m.%Y %k:%M:%S")})
    else:
        write({"date": date.strftime("%d.%m.%Y"), "type": 2, "lastupdate": now.strftime("%d.%m.%Y %k:%M:%S")})

def check_args(args):
    get_data(args)


if __name__ == '__main__':
    check_args(init_argparse())
