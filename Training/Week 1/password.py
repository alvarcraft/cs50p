def main():
    password = input("enter a password ").strip()
    if len(password) > 8:
        print("strong")
    elif 5 <= len(password) < 8:
        print ("medium")
    else:
        print("weak")

main()
