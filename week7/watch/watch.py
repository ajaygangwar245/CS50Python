import re


def main():
    print(parse(input("HTML: ")))


def parse(str):

    # using capture groups we capture URL from src attribute
    pattern = r"^<iframe.* src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\".*></iframe>$"

    # check for match
    match = re.search(pattern, str)

    # if match found return short URL
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
