def greetings():
    greeting = input("Greetings: ").strip().lower().split()
    
    if greeting[0][2] == "l":
        print("$0")

    elif greeting[0][0] == "h":
        print("$20")

    else:
        print("$100")

greetings()