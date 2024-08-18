final_item_list = {}

while True:
    try:
        user_input = input().lower().strip()
        if user_input in final_item_list:
            final_item_list[user_input] += 1
        else:
            final_item_list[user_input] = 1
    except EOFError:
        final_item_list_sorted = sorted(final_item_list.items())
        for item in final_item_list_sorted:
            print(f"{item[1]} {item[0].upper()}")
        break
