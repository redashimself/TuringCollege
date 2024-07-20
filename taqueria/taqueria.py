menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

final_price = 0.00
menu_lowercase = {
    key.lower(): value for key, value in menu.items()
}

while True:
    try:
        user_input = input("Please place your order and press CTRL + D when you're done: ").lower().strip()

        for item in menu_lowercase:
            if user_input == item:
                final_price += menu_lowercase[user_input]

        print(f"Total: ${final_price:.2f}")
    except EOFError:
        break
