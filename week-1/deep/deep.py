def ask():

    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    if question == "42" or question == "forty two" or question == "forty-two":
        print("Yes")
    else:
        print("No")

ask()
