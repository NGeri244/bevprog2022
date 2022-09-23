def mondat(bekerdezes):

    for x in bekerdezes:
        if x in betuk:
            betuk[x] += 1
        else:
            betuk[x] = 1

    print("Betűk gyakorisága: " + str(betuk))

    forditott = bekerdezes[::-1]
    print("Fordítva: " + str(forditott))

    szetszedett = list(bekerdezes.split(" "))
    print("Listába rendezve szavanként: "+ str(szetszedett))

if __name__ == "__main__":
    print("Adjon meg egy mondatot: ")
    bekerdezes = input()
    betuk = {}
    mondat(bekerdezes)