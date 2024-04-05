import math

class kor:
  def __init__(self, r):
    self.r = r
  def kerulet(self):
    return 2 * self.r *math.pi
  def terulet(self):
    return self.r ** 2 * math.pi

r = int(input('Hany centimeter legyen a kor sugara? '))

print(f'A kor kerulete {kor(r).kerulet():.2f}cm.')
print(f'A kor terulete {kor(r).terulet():.2f}cm.')