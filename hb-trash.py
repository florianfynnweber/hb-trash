import requests
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        description="Tool for getting the garbage collection dates in Bremen, Germany as ics or csv")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("-i", "--ical", action="store_true", help="ical format")
    action.add_argument("-c", "--csv", action="store_true", help="csv format")
    # force to get an integer as value
    parser.add_argument("-s", "--street", type=str, help="Name of street")
    parser.add_argument("-n", "--nr", type=str, help="Street number")
    return parser.parse_args()


def get_data(format, args):
    r = requests.post(
        "https://web.c-trace.de/bremenabfallkalender/(S(bipsbtlhddavyhhnypfj2wwp))/abfallkalender/{}?abfall=".format(
            format), params={"strasse": str(args.street), "hausnr": str(args.nr)})
    csv_string = r.content.decode("ISO-8859-1")
    with open("hb-trash.{}".format("ics" if format == "cal" else format), "w") as file:
        file.write(csv_string)


def check_args(args):
    if args.ical:
        get_data("cal", args)
    elif args.csv:
        get_data("csv", args)
    else:
        raise Exception()


if __name__ == '__main__':
    check_args(init_argparse())
