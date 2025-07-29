def main():

    while True:
        try:
            dict = {}
            while True:
                item = input()
                if item in dict:
                    dict[item] = dict[item] + 1
                else:
                    dict[item] = 1


        except EOFError:
                for text in sorted(dict):
                    
                    print(f"{str(dict[text])} {text.upper()}\n", end="")
                break     

main()  