#Расчёт по двум формулам
# 1. z1 = (1+a+a**2/2a+a**2 + 2 - 1-a+a**2/2a-a**2) * (5-2a**2);
#При a1=4 z1=-265.5; a1=3 z1=-161.2; a1=1 z1=2.0; a1=7 z1=-789.4666667; a1=5 z1=-407.1428571;
# 2. z2 = 4-a**2/2;
#При a2=8 z2=-30.0; a2=1 z2=1.5; a2=6 z2=-16.0; a2=10 z2=-48.0; a2=24 z2=-286.0;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
tmp = a1 ** 2
tmp1 = 2 * a1
tmp3 = tmp1 ** 2

z1 = (((1 + a1 + tmp) / (tmp1 + tmp)) + 2 - ((1 - a1 + tmp) / (tmp1 - tmp))) * (5 - tmp3)
z2 = (4 - (a2 ** 2)) / 2

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))