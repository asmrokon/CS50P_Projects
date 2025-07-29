def main():
    greeting = input("Greetings: ").strip().lower().split()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting[0][2] == "l":
        if greeting[0][0] == "h":
            if greeting[0][3] == "l":
                return 0

    elif greeting[0][0] == "h":
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
