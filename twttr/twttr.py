user_input = input("What would you like to twt about? ").strip()

for vowel in "aeiouAEIOU":
    user_input = user_input.replace(vowel, "")

print(user_input)
