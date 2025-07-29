import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += game(x, y)
    print(f"Score: {score}")


def game(x, y):
    score = 0
    fail = 0
    while True:
        try:
            answer = input(f"{x} + {y} = ")
            if int(answer) == (x + y):
                score += 1
                break
            if int(answer) != (x + y):

                fail = fail + 1
                print("EEE")
                if fail == 3:
                    fail = fail - 3
                    print(f"{x} + {y} = {(x + y)}")
                    break
        except ValueError:
            fail = fail + 1
            print("EEE")
            if fail == 3:
                fail = fail - 3
                print(f"{x} + {y} = {(x + y)}")
                break
    # print(f"Score: {score}")
    return score


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
    return x


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


if __name__ == "__main__":
    main()
