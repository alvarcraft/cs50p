def main():
    km = input("insert km: ")
    meters = convert(km)
    print(f"{meters:.2f}")

def convert(km):
    return float (km) * 0.621371

main()
