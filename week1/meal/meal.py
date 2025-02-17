def main():
    time = input("What time is it? ")
    numTime = convert(time)

    if numTime >= 7 and numTime <= 8:
        print("breakfast time")
    elif numTime >= 12 and numTime <= 13:
        print("lunch time")
    elif numTime >= 18 and numTime <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = round(float(minutes) / 60, 2)
    return float(hours) + minutes


if __name__ == "__main__":
    main()
