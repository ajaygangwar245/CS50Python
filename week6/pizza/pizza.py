import csv
import sys
from tabulate import tabulate


def main():
    # No filename entered
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # Many filename entered
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Wrong file extension entered
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # print price table
    else:
        print(price_table(sys.argv[1]))


def price_table(filename):
    try:
        # file opened and read using csv reader
        with open(filename, "r") as file:
            table = csv.reader(file)

            # tabulate function converts data into ASCII table
            return tabulate(table, headers="firstrow", tablefmt="grid")

    # File does not exists in folder
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
