def main():
    inputs = input("Input: ")
    inputs = remove_vowel(inputs)
    print(f"Output: {inputs}")

def remove_vowel(t):
    
    vowels = ["a", "e", "i", "o", "u"]

    for vowel in vowels:
        t = t.replace(vowel, "")
    return t

main()