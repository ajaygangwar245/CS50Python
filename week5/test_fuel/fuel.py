def main():
    fuel = input("Fraction: ")
    percent = convert(fuel)
    print(gauge(percent))


def convert(fraction):
    x, y = fraction.split(sep="/")
    if int(x) / int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    elif 99 <= percentage <= 100:
        return "F"


if __name__ == "__main__":
    main()
