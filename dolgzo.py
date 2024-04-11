print('3. feladat')

class Dolgozo:
    def __init__(self, nev, szemelyig, osszesszabad, kivettszabad):
        self.nev = nev
        self.szemelyig = szemelyig
        self.osszesszabad = osszesszabad
        self.kivettszabad = kivettszabad
    def maradekSzabadsagSzamol(self):
        return self.osszesszabad - self.kivettszabad
    def adatokKiir(self):
        print(f'Nev: {self.nev}, szig. szam:{self.szemelyig}, osszes szabadsag: {self.osszesszabad}, kivett szabadsag: {self.kivettszabad}, maradek szabadsag: {self.maradekSzabadsagSzamol()}')

adatok = []
for i in range(3):
    adatok.append(Dolgozo(input(f'Adja meg a(z) {i+1}. dolgozo nevet: \n'), input(f'Adja meg a(z) {i+1}. dolgozo szig. szamat: \n'), int(input(f'Adja meg a(z) {i+1}. dolgozo osszes szabadsagat \n')), int(input(f'Adja meg a(z) {i+1}. dolgozo kivett szabadsagat: \n'))))

for i in adatok:
    i.adatokKiir()