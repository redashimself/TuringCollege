import re
import sys


def main():
    user_input = input("HTML: ")

    pattern = r'src="(?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/embed/([a-zA-Z0-9_-]{11})"'
    match = re.search(pattern, user_input)

    if match:
        video_id = match.group(1)
        print(f"https://youtu.be/{video_id}", end='')
    else:
        print("None", end='')


if __name__ == "__main__":
    main()
