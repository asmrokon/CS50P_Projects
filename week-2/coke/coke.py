def main():

    amount_due = 50
    while amount_due > 0:
        coin = int(input("Insert Coin: "))
        if coin == 25:
            amount_due = amount_due - coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        elif coin == 5:
            amount_due = amount_due - coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        elif coin == 10:
            amount_due = amount_due - coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        else:
            print(f"Amount Due: {amount_due}")

    if amount_due <= 0:
       change_owned = abs(amount_due)
       print(f"Change Owed: {change_owned}") 



main()
