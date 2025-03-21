import re


def main():
    print(convert(input("Hours: ")))


def convert(hrs):
    pattern = r"^(0?[0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$"

    match = re.search(pattern, hrs)

    if match:
        hrs1 = match.group(1)
        mins1 = match.group(2)
        ampm1 = match.group(3)
        time1 = format_time(hrs1, mins1, ampm1)

        hrs2 = match.group(4)
        mins2 = match.group(5)
        ampm2 = match.group(6)
        time2 = format_time(hrs2, mins2, ampm2)

        return f"{time1} to {time2}"

    else:
        raise ValueError


def format_time(hr, min, ampm):
    if hr == "12":
        if ampm == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if ampm == "AM":
            hr = f"{int(hr):02}"
        else:
            hr = f"{int(hr)+12}"

    if min == None:
        min = "00"
    else:
        min = f"{int(min):02}"

    return f"{hr}:{min}"


if __name__ == "__main__":
    main()
