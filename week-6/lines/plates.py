def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Define if it is vaild or not
# Define if it is vaild or not
# Define if it is vaild or not
# Define if it is vaild or not
# Define if it is vaild or not
# Define if it is vaild or not


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            if s.isalnum():
                if s.isalpha():
                    return True
                else:
                    for t, d in enumerate(s):
                        if d.isdigit():
                            if d == "0":
                                return False
                            if s[t:].isdigit():
                                return True
                            else:
                                return False

    else:
        return False


if __name__ == "__main__":
    main()
