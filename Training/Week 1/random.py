def main():
    name = input("What's your name? ")
    time = input("Time of day (morning/afternoon/evening)? ")
    print(greet(name, time))


def greet(name, time):
    return f"Good {time}, {name.title()}"

main()
