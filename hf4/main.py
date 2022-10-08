def szamolas():
    while(True):
        try:
            a = int(input("Enter 'a' value: "))
            b = int(input("Enter 'b' value: "))
            c = float(a/b)
        except ZeroDivisionError:
            print("Division by zero not alowed")
            print("Out of try except blocks")
        else:
            print(c)
            print("Out of try except blocks")

if __name__ == "__main__":
    szamolas()
