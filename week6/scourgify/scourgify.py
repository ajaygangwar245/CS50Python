import csv
import sys


def main():
    # No filename entered
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Many filename entered
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Wrong file extension entered
    elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a csv file")

    # Open file and read
    else:
        clean_file(sys.argv[1], sys.argv[2])


def clean_file(input, output):
    try:
        with open(input, "r") as before, open(output, "w") as after:
            # reads file
            reader = csv.DictReader(before)

            # writes to file
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])

            # writes header to 'after' file
            writer.writeheader()

            # reading each row of 'before' file
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]

                # Writes row to 'after' file
                writer.writerow({"first": first.lstrip(), "last": last, "house": house})

    # file not found error
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


main()
