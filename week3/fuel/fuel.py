def main():
    fuel = get_percentage("Fraction: ")
    print(fuel)


def get_percentage(prompt):
    while True:
        try:
            x, y = input(prompt).split(sep="/")
            fraction = int(x) / int(y)
            if 0 <= fraction <= 0.1:
                return "E"
            elif 0.1 < fraction < 0.9:
                return str(round(fraction * 100)) + "%"
            elif 0.9 <= fraction <= 1:
                return "F"
        except (ValueError, ZeroDivisionError):
            pass


main()
