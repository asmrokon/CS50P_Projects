def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if  not s.isalnum():
        return False
    for i, d in enumerate(s):
        if d.isdigit():
            if d == "0":
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


main()