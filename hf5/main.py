class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor
        print("-- Developer létrehozva. --")

    def __str__(self):
        return f"{self.nev} a {self.projekt}-en dolgozik {self.szerepkor} szerepkörben."

    def __eq__(self, masik):
       return self.projekt == masik.projekt

emberek = []
e1 = Team("Ricsi", "SolArch","Frontend")
emberek.append(e1)
print(e1)
e2 = Team("Angéla","ZerTeng","Tesztelo")
emberek.append(e2)
print(e2)
e3 = Team("Peti","KefERP","Backend")
emberek.append(e3)
print(e3)
e4 = Team("Éva","KefERP","Frontend")
emberek.append(e4)
print(e4)

for emb in emberek:
    for proj in emberek:
        if emb.projekt == proj.projekt:
            if emb.nev != proj.nev or proj.nev != emb.nev:
                csapat = []
                csapat.append(emb.nev)
                csapat.append(proj.nev)
                


print (f"\n{csapat[0]} és {csapat[1]} ugyanazon a projekten dolgozik.")


