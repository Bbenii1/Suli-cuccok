class Medence:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b        
        self.c = c

    def alap(self):
        return self.a * self.b
    def terfogat(self):
        return self.a * self.b * self.c
    def felulet(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

medencek = [Medence(20, 40, 3),  Medence(5, 5, 0.8), Medence(20, 20, 2), Medence(8, 5, 1.5), Medence(2, 2, 2)]

def alapAtlag(medencek):
    atlag = 0
    for i in medencek:
        atlag += Medence.alap(i)
    print(f"A medencék átlagos alapterülete {atlag / len(medencek)} négyzetméter.")

def feltoltes(medencek):
    ossz = 0
    for i in medencek:
        ossz += Medence.terfogat(i)
    print(f"{ossz} mköbméter víz kell, hogy mindegyik medence teljesen fel legyen töltve.")

def legmelyebbMedence(medencek):
    mely = medencek[0].c
    index = 1
    for i in range(len(medencek)):
        if medencek[i].c > mely:
            mely = medencek[i]
            index += 1
    print(f"A legmélyebb medence a(z) {index}. medence.")

def csempezheto(medencek):
    limit = 1000
    van = 0
    for j in range(len(medencek)):
        terulet = Medence.felulet(medencek[j]) - medencek[j].a * medencek[j].b
        if terulet > limit:
           van += 1
    if van != 0:
        print("Van olyan medence, amit nem lehet lecsempézni 1000 négyzetméter csempével.")
    else:
        print("Mindegyik medencét le lehet csempézni 1000 négyzetméter csempével.")



alapAtlag(medencek)
feltoltes(medencek)
legmelyebbMedence(medencek)
csempezheto(medencek)
