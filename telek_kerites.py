def KeritesSzamol(a, b):
    return (a + b) * 2

print('2. feladat')

a = float(input('Kerem adj meg a telek egyik oldalat (meter): '))
b = float(input('Kerem adja meg a telek masik oldalat (meter): '))

print(f'Ennyi kerites kell ehhez a telekhez: {KeritesSzamol(a, b)} m')