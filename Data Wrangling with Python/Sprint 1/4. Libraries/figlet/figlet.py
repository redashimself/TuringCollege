import sys
import random
from pyfiglet import Figlet, FontNotFound

figlet = Figlet()
figlet.getFonts()

try:
    if len(sys.argv) == 1:
        user_input = input("Enter a string: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))

        print(figlet.renderText(user_input))
    elif (len(sys.argv) == 3
          and sys.argv[1] == "-f"
          or sys.argv[1] == "--font"):

        figlet.setFont(font=sys.argv[2])

        user_input = input("Enter a string: ")
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid command line arguments")
except FontNotFound:
    sys.exit("Invalid command line arguments")
