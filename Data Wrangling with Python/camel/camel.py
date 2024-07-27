user_input = input("Please write a variable in camelCase")

user_input = user_input.strip()

for letter in user_input:
    if letter.isupper():
        user_input = user_input.replace(letter, f"_{letter.lower()}")

print(user_input)
