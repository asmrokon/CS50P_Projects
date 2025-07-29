import sys
import csv
from tabulate import tabulate


def main():
    list = []
    try:
        if len(sys.argv) == 2:
            if ".csv" in sys.argv[1]:
                try:
                    with open(f"{sys.argv[1]}", "r") as file:
                        for line in csv.reader(file):
                            list.append(line)
                    table = ascii(list)
                    print(table)
                except FileNotFoundError:
                    sys.exit("File does not exist")
            else:
                raise FileNotFoundError
        elif len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("Not a CSV file")


def ascii(list):
    headers = list[0]
    content = list[1:]
    asc = tabulate(content, headers, tablefmt="rounded_grid")
    return asc


main()
