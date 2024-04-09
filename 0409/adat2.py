szoveg = open('adat2.txt', 'r', encoding="utf-8")

jegyek = szoveg.readlines()

class Diak:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = jegyek

    def jegy(self, jegyek):
        self.jegyek = jegyek
    
    def atlag(self):
        ossz = 0
        for i in range(len(jegyek)):
            ossz = ossz + self.jegyek[i]
        return round(ossz / len(jegyek), 2)

diakok = [Diak('Dani', []), Diak('Peti', []), Diak('Kati', []), Diak('Tomi', []), Diak('Feri', [])]

for i in range(len(jegyek)):
    jegyek[i] = jegyek[i].strip().split()
    for j in range(len(jegyek[i])):
        jegyek[i][j] = int(jegyek[i][j])

for i in range(len(diakok)):
    diakok[i].jegy(jegyek[i])
    print(diakok[i].nev, diakok[i].jegyek, diakok[i].atlag())


#jegy_tomb = jegyek.split(' ')
#print(jegy_tomb)