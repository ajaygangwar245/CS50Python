import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(mail):
    if validators.email(mail) == True:
        return f"valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
