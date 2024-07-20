import inflect

inflect = inflect.engine()
names = ""
names_list = {}

while True:
    try:
        user_input = input()

        if len(names) == 0:
            names = user_input
        else:
            names = names + "," + user_input

        names_list = names.split(",")
    except EOFError:
        print(f"Adieu, adieu, to {inflect.join(names_list)}")
        break
