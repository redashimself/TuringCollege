import re


def main():
    print(convert(input("Hours: ")))


def convert(user_input):
    pattern = r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)$'
    match = re.match(pattern, user_input)

    if not match:
        raise ValueError("Invalid input format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_min = int(start_min or 0)
    end_min = int(end_min or 0)

    if start_period == 'PM' and start_hour != 12:
        start_hour += 12
    elif start_period == 'AM' and start_hour == 12:
        start_hour = 0

    if end_period == 'PM' and end_hour != 12:
        end_hour += 12
    elif end_period == 'AM' and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02d}:{start_min:02d} to {end_hour:02d}:{end_min:02d}"


if __name__ == "__main__":
    main()
