#Расчёт по двум формулам
# 1. z1 = cos**2(3/8pi - a/4) - cos**2(11/8pi + a/4);
#При а1=4 z1=0.6429704; a1=2 z1=0.5950098; a1=-1 z1=-0.3390050; a1=7 z1=-0.2480412; a1=-5 z1=-0.4231837;
# 2. z2 = sqrt(2)/2sina/2;
#При а2=2 z2=0.5950098; a2=-1 z2=-0.3390050; a2=6 z2=0.0997869; a2=10 z2=-0.6780619; a2=24 z2=-0.3794143;

from math import *

a1 = float(input('Введите параметр а1 = '))
a2 = float(input('Введите параметр а2 = '))

z1 = (cos(3/8 * pi - a1/4) ** 2) - (cos(11/8 * pi + a1/4) ** 2)
z2 = sqrt(2)/2 * sin(a2/2)

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))