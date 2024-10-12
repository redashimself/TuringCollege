import emoji

user_input = input()

print(emoji.emojize(f"{user_input}", language='alias').lower().strip())
