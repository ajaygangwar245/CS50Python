def main():
    txt = input("Input: ")
    new_txt = shorten(txt)
    print(f"Output: {new_txt}")


def shorten(str):
    short_txt = ""
    for c in str:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            short_txt += c

    return short_txt


if __name__ == "__main__":
    main()
