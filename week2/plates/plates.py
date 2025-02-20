def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # No periods, spaces, or punctuation marks are allowed
    # Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters
    if s.isalnum() and 2 <= len(s) <= 6:

        # all characters are alphabets
        if s.isalpha():
            return True
        else:
            # All vanity plates must start with at least two letters
            if s[0:2].isalpha() and s[-2:].isdigit():

                # Numbers cannot be used in the middle of a plate
                # The first number used cannot be a ‘0’
                for i in range(len(s)):
                    if s[i].isdigit():
                        # Return True if number in middle of letters
                        if s[i] == "0" or s[i:].isalpha():
                            return False
                        else:
                            return True

            else:
                return False

    else:
        return False


main()
