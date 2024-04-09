szoveg = open('adat1.txt', 'r', encoding="utf-8")

jegyek = szoveg.readlines()
osszeg = 0

for i in range(len(jegyek)):
    jegyek[i] = jegyek[i].strip()
    osszeg = osszeg + int(jegyek[i])


print(jegyek)
print(f'Az atlag: {osszeg / len(jegyek)}')