import re


def main():
    print(count(input("Text: ")))


def count(str):
    pattern = r"(^|\W)um($|\W)"

    match = re.findall(pattern, str, re.IGNORECASE)

    return len(match)


if __name__ == "__main__":
    main()
