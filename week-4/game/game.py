import random
import sys

def main():
    # promtps for a number
    while True:
        try:
            num = int(input("Level: "))
            if num > 0:
                break
        except ValueError:
            pass
    # generates an integer
    to_num = random.randint(1, num)

    # prompts the user to guess the integer
    while True:
        try:
            game(to_num)
            break
        except ValueError:
            pass

def game(tn):
    while True:
        n = int(input("Guess: "))

        if n > 0:
            if n > tn:
                print("Too large!")
            elif n < tn:
                print("Too small!")
            elif n == tn:
                print("Just right!")
                break


main()
sys.exit()