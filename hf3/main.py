def kiszamitas():
    if a < (b + c) and b < (a + c) and c < (b + a):
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög szerkeszthető.")
    else:
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög NEM szerkeszthető.")



if __name__ == "__main__":
    print("Adja meg a háromszög három oldalát cm-ben: ")
    a = int(input())
    b = int(input())
    c = int(input())
    kiszamitas()

