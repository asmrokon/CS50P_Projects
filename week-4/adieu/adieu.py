import inflect
p = inflect.engine()
def main():
    try:
        name_list = []
        while True:
            name = input()
            name_list.append(name)

    except EOFError:
        print(f"Adieu, adieu, to {p.join(name_list)}")
main()
    