def main():
    grocery = {}

    while True:
        try:
            item = input()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except KeyError:
            pass
        except EOFError:
            for items in sorted(grocery):
                print(f"{grocery[items]} {items.upper()}")
            break


main()
