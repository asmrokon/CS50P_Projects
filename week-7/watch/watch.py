import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        code = re.search(
            r'<iframe.*src="https?://(www\.)?youtube\.com/embed/(?P<video_code>\w+)".*</iframe>',
            s,
        )
        url = "https://youtu.be/" + code.group("video_code")
        return url
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
