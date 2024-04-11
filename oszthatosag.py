print('1. feladat')
x = 0

while x < 3:
    a = int(input('Kerem adja meg a(z) 1. szamot: '))
    if a % 3 == 0 and a % 5 == 0:
        print('Oszthato harommal es ottel maradek nelkul.')
    else:
        print('NEM oszthato harommal es ottel maradek nelkul.')
    x += 1