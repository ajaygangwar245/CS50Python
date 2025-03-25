import inflect
import sys
import operator
from datetime import date


def main():
    # ask user for input his date of birth
    dob = input("Date of Birth: ")

    # mumber of days from DOB to today
    days = count_days(dob)

    # prints by converting days into minutes
    print(convert(days))


def count_days(birth_date):
    try:
        # today's date
        today_date = date.today()

        # date of birth in date ISO format i.e., YYYY-MM-DD
        from_date = date.fromisoformat(birth_date)

        # difference of days using sub operator
        diff = operator.sub(today_date, from_date)

        # returning number of day
        return diff.days

    # except the error if user enters invalid date
    except ValueError:
        sys.exit("Invalid Date")


def convert(dayCount):

    # object of inflect engine
    p = inflect.engine()

    # convert days to minutes
    minutes = dayCount * 24 * 60

    # returns f string of minutes without 'and' word in it
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
