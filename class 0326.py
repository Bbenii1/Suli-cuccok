class Allatkert:
    def __init__(self, nev):
        self.nev = nev
        self.allatok = []

    def uj_allat(self, allatok):
        self.allatok.append(allatok)

    def kiir(self):
        nevek = [elem.nev for elem in self.allatok]
        return nevek
    
class Allatok:
    def __init__(self, nev, fajta, kor):
        self.nev = nev
        self.fajta = fajta
        self.kor = kor

allatkert = Allatkert("Zoo")
allat1 = Allatok("Buxu", "majom", 9)
allat2 = Allatok("Gígyó", "python", 3)

allatkert2 = Allatkert("masik allatkert")
allat3 = Allatok("Horatius", "majom", 48)

allatkert.uj_allat(allat1)
allatkert.uj_allat(allat2)
allatkert2.uj_allat(allat3)

print(allatkert.kiir())
print(allatkert2.kiir())

while True:
    nev = input("Új állat neve: ")
    fajta = input("Új állat fajtája: ")
    kor = input("Új állat kora: ")

    uj_allat = Allatok(nev, fajta, kor)
    allatkert.uj_allat(uj_allat)

    folytatja = input("Y/N?: ").lower()
    if folytatja != "y":
        print("Az állatkert állatainak nevei:")
        for allat in allatkert.allatok:
            print(f"Név: {allat.nev}, Kor: {allat.kor}")
        break