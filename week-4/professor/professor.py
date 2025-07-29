import random

def main():
    level = get_level()
    questions = generate_integer(level)
    score = 0
    false = 0
    for que, ans in questions.items():
        while True:
            try:
                answer = input(f"{que} = ")
                if int(answer) == ans:
                    score += 1
                    break
                if int(answer) != ans:

                    false = false + 1
                    print("EEE")
                    if false == 3:
                        false = false - 3
                        print(f"{que} = {ans}")
                        break
            except ValueError:
                false = false + 1
                print("EEE")
                if false == 3:
                    false = false - 3
                    print(f"{que} = {ans}")
                    break
    print(f"Score: {score}")


def generate_integer(level):
    if level == 1:
        num_list = {}
        numbers_1 = random.sample(range(0, 10), k=10)
        numbers_2 = random.sample(range(0, 10), k=10)
        for n1, n2 in zip(numbers_1, numbers_2):
            if len(num_list.keys()) < 10:
                n_answer = n1 + n2
                single_list = {f"{n1} + {n2}": n_answer}
                num_list.update(single_list)
        return num_list
    elif level == 2:
        num_list = {}
        numbers_1 = random.sample(range(10, 100), k=10)
        numbers_2 = random.sample(range(10, 100), k=10)
        for n1, n2 in zip(numbers_1, numbers_2):
            if len(num_list.keys()) < 10:
                n_answer = n1 + n2
                single_list = {f"{n1} + {n2}": n_answer}
                num_list.update(single_list)
        return num_list
    elif level == 3:
        num_list = {}
        numbers_1 = random.sample(range(100, 1000), k=10)
        numbers_2 = random.sample(range(100, 1000), k=10)
        for n1, n2 in zip(numbers_1, numbers_2):
            if len(num_list.keys()) < 10:
                n_answer = n1 + n2
                single_list = {f"{n1} + {n2}": n_answer}
                num_list.update(single_list)
        return num_list


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
