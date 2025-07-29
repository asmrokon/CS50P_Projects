expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    a = x + z
    print(f"{a:.1f}")

elif y == "-":
    a = x - z
    print(f"{a:.1f}")

elif y == "*":
    a = x * z
    print(f"{a:.1f}")

elif y == "/" and z != 0:
    a = x / z
    print(f"{a:.1f}")

