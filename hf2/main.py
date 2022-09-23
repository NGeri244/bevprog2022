
def szamitas(veglegesSzam):
    veglegesSzam = bekertSzam
    vegeredmeny = 0
    if mertekE == "cm" or mertekE == "inch":
        if mertekE == "cm":
            vegeredmeny = float(veglegesSzam) * 0.393700787
            print(str(vegeredmeny) + " inches")
        else:
            vegeredmeny = float(veglegesSzam) / 0.393700787
            print(str(vegeredmeny) + " centimeters")
    else: print("Not correct unit!")

if __name__ == "__main__":
    print("Adjon meg egy számot és egy mértékegységet (cm/inch): ")
    bekertSzam = int(input())
    mertekE = str(input())
    mertekE = mertekE.lower()
    szamitas(bekertSzam)
    