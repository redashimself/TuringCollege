# https://www.hackerrank.com/challenges/validating-uid/problem
user_input = "2\nB1CD102354\nB1CDEF2354\nb1cdef2354"


class Validator:
    def __init__(self, uid):
        self.row = uid

    @staticmethod
    def contains_two_uppercase_characters(uid):
        count = 0
        for character in uid:
            if character.isupper():
                count += 1
        if count >= 2:
            return True
        return False

    @staticmethod
    def contains_three_digits(uid):
        count = 0
        for character in uid:
            if character.isdigit():
                count += 1
        if count >= 3:
            return True
        return False

    @staticmethod
    def contains_only_alphanumeric_characters(uid):
        for character in uid:
            if character.isdigit() or character.isalpha():
                continue
            else:
                return False
        return True

    @staticmethod
    def does_not_have_repeating_characters(uid):
        # If not working, is number a character?
        existing_char_list = []
        for character in uid:
            if existing_char_list.__contains__(character):
                return False
            existing_char_list.append(character)
        return True

    @staticmethod
    def has_exactly_ten_characters(uid):
        if len(uid) == 10:
            return True
        return False


input_list = user_input.split("\n")

for row in input_list:
    if input_list[0] == row:
        continue

    if Validator.contains_two_uppercase_characters(row) \
            and Validator.contains_three_digits(row) \
            and Validator.contains_only_alphanumeric_characters(row) \
            and Validator.does_not_have_repeating_characters(row) \
            and Validator.has_exactly_ten_characters(row):
        print("Valid")
    else:
        print("Invalid")
