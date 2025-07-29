import sys


def main():
    try:
        if len(sys.argv) == 2:
            if ".py" in sys.argv[1]:
                try:
                    with open(f"{sys.argv[1]}", "r") as file:
                        count_lines = count(file)
                        print(count_lines)
                except FileNotFoundError:
                    sys.exit("File does not exist")
            else:
                sys.exit("Not a Python file")
        elif len(sys.argv) == 1:
            raise IndexError
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("Not a Python file")
    except IndexError:
        sys.exit("Too few command-line arguments")


def count(f):
    lines = {"lines": 0}
    for line in f:
        if not line.strip().startswith("#"):
            if line.strip():
                lines["lines"] += 1
    return lines["lines"]


main()
