import datetime
import sys
from datetime import date
import inflect


def get_user_date():
    try:
        user_input = input("Please enter your birthdate: ")
        users_birthdate = datetime.datetime.strptime(user_input, "%Y-%m-%d")

        return users_birthdate
    except ValueError:
        print("Invalid date. Please enter a valid date.")
        sys.exit(1)


def get_now():
    today = date.today()
    return datetime.datetime.strptime(str(today), "%Y-%m-%d")


def get_minutes_between_dates(user_date, now):
    return (now - user_date).days * 24 * 60


def main():
    user_date = get_user_date()
    now = get_now()

    result = get_minutes_between_dates(user_date, now)

    minutes_to_words = inflect.engine().number_to_words(result, andword="").capitalize()

    print(f"{minutes_to_words} minutes")


if __name__ == "__main__":
    main()
