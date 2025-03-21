import re


def main():
    print(validate(input("IPV4 Address: ")))


def validate(ip):
    # regex for every octet of ipv4 is divided in 3 parts ([0-1]?([0-9]?){2} | 2[0-4]?[0-9]? | 25[0-5]?)
    # [0-1]?([0-9]?){2} represents numbers 0 - 199
    # 2[0-4]?[0-9]? represents numbers 200 - 249
    # 25[0-5]? represents numbers 250 - 255
    pattern = r"^(([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)\.){3}([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)$"

    # check if pattern is matched or not
    match = re.search(pattern, ip)

    # return true if pattern matched else return false
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
