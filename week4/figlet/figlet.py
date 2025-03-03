from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

# get list of fonts from figlet library
fonts = figlet.getFonts()

# checks for 2 valid command-line arguments
if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])

# checks for 0 command-line argument
elif len(sys.argv) == 1:
    randFont = random.choice(fonts)
    figlet.setFont(font=randFont)

# terminates program if invalid command-line arguments entered
else:
    sys.exit("Invalid Usage")

# prompts user for text input
text = input("Input: ").strip()

# prints text in figlet ASCII fonts
print(figlet.renderText(text))
