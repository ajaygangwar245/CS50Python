import sys
import os
from PIL import Image, ImageOps


def main():
    # No filename entered
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Many filename entered
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        extns = [".jpeg", ".jpg", ".png"]
        extn1 = os.path.splitext(sys.argv[1])
        extn2 = os.path.splitext(sys.argv[2])

        # Invalid input file extension
        if extn1[1].lower() not in extns:
            sys.exit("Invalid input")

        # Invalid output file extension
        elif extn2[1].lower() not in extns:
            sys.exit("Invalid output")

        # Different file extension entered
        elif extn1[1].lower() != extn2[1].lower():
            sys.exit("Input and output have different extensions")

        # Apply overlay on image file
        else:
            img_overlay(sys.argv[1], sys.argv[2])


def img_overlay(inputFile, outputFile):
    try:

        # opened shirt image
        shirt = Image.open("shirt.png")

        # size tuple of shirt image
        size = shirt.size

        # opened input file to edit
        with Image.open(inputFile) as input:

            # made input file fit the size of shirt image
            img = ImageOps.fit(input, size)

            # pasted shirt file on input file
            img.paste(shirt, mask=shirt)

            # saved edited image to output file
            img.save(outputFile)

    # file not found error
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
