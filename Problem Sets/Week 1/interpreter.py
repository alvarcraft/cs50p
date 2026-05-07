expression = input("Expression: ").split()
x = float(expression[0])
y = expression[1]
z = float(expression[2])
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print (f"{x - z:.1f}")
elif y == "/":
    print (f"{x / z:.1f}")
elif y == "*":
    print (f"{x * z:.1f}")
