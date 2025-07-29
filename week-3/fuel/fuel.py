def main():

    while True:
        try:
            fraction = input("Fraction: ")
            fraction = fraction.split("/")
            fuel = round((int(fraction[0]) / int(fraction[1])) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if 100 >= fuel >= 1:
                break

    if fuel <= 1:
        print("E")
    elif 100 >= fuel >= 99:
        print("F")

    else:
        print(f"{fuel}%")
    
main()
