import re
import sys


def main():
    ip = input("IPv4 Address: ")
    validation = validate(ip)
    print(validation)


def validate(ip):
    if num := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if (
            0 <= int(num.group(1)) <= 255
            and 0 <= int(num.group(2)) <= 255
            and 0 <= int(num.group(3)) <= 255
            and 0 <= int(num.group(4)) <= 255
        ):
            if not re.search(r"\b0[0-9]+\b", ip):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
