import sys


def main():
    # No filename entered
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # Many filename entered
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Wrong file extension entered
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    # count lines
    else:
        print(count_lines(sys.argv[1]))


def count_lines(filename):
    count = 0
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            # Ignore file starts with '#' (i.e., comments) or lines that only consist white spaces
            for line in lines:
                if line.lstrip().startswith("#") or not (line and line.strip()):
                    continue
                else:
                    count += 1
        return count

    # file not found error
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
