userInput = input("What's the Ultimate Answer to Life, The Universe, and Everything?")
userInput = userInput.lower().strip()

if userInput == "42" or userInput == "forty-two" or userInput == "forty two":
    print("Yes")
else:
    print("No")
