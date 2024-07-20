def main():
    user_input = input("What would you like to twt about? ").strip()

    print(shorten(user_input))


def shorten(user_input):
    for vowel in "aeiouAEIOU":
        user_input = user_input.replace(vowel, "")
    return user_input


if __name__ == "__main__":
    main()
