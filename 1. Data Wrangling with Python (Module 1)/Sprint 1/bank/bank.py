userInput = input("Hi!")
userInput = userInput.strip().lower()

if userInput.startswith("hello"):
    print("$0")
elif userInput.startswith("h"):
    print("$20")
else:
    print("$100")
