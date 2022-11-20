import string
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U','Á','É','Í','Ú','Ű','Ö','Ü','Ó','í','é','á','ű','ő','ú','ö','ü','ó']
vegeredmeny = ""
with open("hazi.txt","r",encoding="UTF-8") as szoveg:
 for i in szoveg.readlines():
        if not i.strip():
            continue
        if i:
            asd = i.translate(str.maketrans('', '', string.punctuation))
            vegeredmeny = vegeredmeny + asd
            print(vegeredmeny)



with open("veg.txt","w") as kiiratas:
    kiiratas.write(vegeredmeny)

