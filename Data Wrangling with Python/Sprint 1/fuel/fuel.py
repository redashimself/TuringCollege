while True:
    try:
        user_input = input("How much fuel is left as a fraction X/Y? ").strip()
        fuel = user_input.split("/")

        x = int(fuel[0])
        y = int(fuel[1])

        remaining_fuel = x / y * 100
        remaining_fuel = round(remaining_fuel)

        if x > y:
            print("X is greater than Y")
            continue
        elif y == 0:
            print("Y is 0")
            continue
        elif remaining_fuel == 1 or remaining_fuel == 0:
            print("E")
        elif remaining_fuel == 99 or remaining_fuel == 100:
            print("F")
        else:
            print(f"{remaining_fuel}%")
    except (ValueError, ZeroDivisionError, IndexError):
        print("Something wrong with fraction format")
    else:
        break
