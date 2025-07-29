calories = {
        "apple": 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100 
            }

def main():  

 

    item = input("Item: ").lower()
    if item not in calories:
        print()
    else:
        fruits_calories = cal(item)
        print(f"Calories: {fruits_calories}")

def cal(i):
    for fruit in calories:
        if fruit == i:
            return calories[i]

main()
