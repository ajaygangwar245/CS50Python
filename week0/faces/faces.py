def main():
    text = input()
    newText = convert(text)
    print(newText)


def convert(txt):
    if ":)" or ":(" in txt:
        return txt.replace(":)", "\U0001f642").replace(":(", "\U0001f641")
    else:
        return txt


main()
