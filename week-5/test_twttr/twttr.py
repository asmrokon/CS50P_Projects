def main():
    inputs = input("Input: ")
    inputs = shorten(inputs)
    print(f"Output: {inputs}")


def shorten(t):

    vowels = ["a", "e", "i", "o", "u"]

    for vowel in vowels:
        t = t.replace(vowel, "")
        t = t.replace(vowel.upper(), "")
    return t


if __name__ == "__main__":
    main()
