import requests
import sys


def main():
    # exit program if exact command-line argument not provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            # convert string value of Command-line argument to float
            num = float(sys.argv[1])

            # calls function and prints total amount
            print(total_amount(num))
        except ValueError:
            sys.exit("Command-line argument is not a number")


def total_amount(n):
    try:
        # request made to API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # JSON response stored in object
        obj = response.json()

        # Access the price part of object
        price = obj["bpi"]["USD"]["rate_float"]

        # calculate total amount
        amount = price * n

        # return formatted amount to main() upto 4 decimals
        return f"${amount:,.4f}"
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
