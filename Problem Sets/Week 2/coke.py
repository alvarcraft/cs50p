coke = 50
while coke > 0:
    coin = int(input(f"Amount Due: {coke}\nInsert Coin: "))
    if coin in [25, 10, 5]:
        coke -= coin
print(f"Change Owed: {abs(coke)}\n")
