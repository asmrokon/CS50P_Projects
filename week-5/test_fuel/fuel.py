import sys


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x = convert(fraction)
            print(gauge(x))
            return True
        except ValueError:
            sys.exit("ValueError")

        except ZeroDivisionError:
            sys.exit("ZeroDivisionError")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    elif x < 0:
        raise ValueError
    elif y < 0:
        raise ValueError
    else:
        z = x / y * 100

        return round(z)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
