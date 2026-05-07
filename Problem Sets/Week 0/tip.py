def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#pitää muuttaa likiluvuks, eli poista dollari merkki ja tee floatti
def dollars_to_float(d):
    return float(d.replace("$",""))

#prosenttiki pitää muuttaa likiluvuks, eka floattii et saadaa desimaali sit poista se % merkki replaceemalla se "" ja jaa sadalla
def percent_to_float(p):
    return float(p.replace("%","")) / 100
#returnii käytetää kosk lasketaa jotai, aina ja print jos ei
main()
