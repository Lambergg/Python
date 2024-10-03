#Расчёт по двум формулам
# 1. z1 = sqrt((3m + 2)**2 - 24m) / 3sqrt(m) - 2/sqrt(m);
#При m1=4 z1=2; m1=2 z1=1.4142136; m1=13 z1=3.6055513; m1=7 z1=2.6457513; m1=5 z1=2.2360680;
# 2. z2 = sqrt(m);
#При m2=2 z2=1.4142136; m2=13 z2=3.6055513; m2=6 z2=2.4494897; m2=10 z2=3.1622777; m2=24 z2=4.8989795;

from math import *

m1 = float(input('Введите параметр m1 = '))
m2 = float(input('Введите параметр m2 = '))
tmp = ((3 * m1) + 2)**2
tmp1 = 24 * m1
tmp2 = (3 * sqrt(m1))
tmp3 = (2 / sqrt(m1))

z1 = sqrt(tmp - tmp1) / (tmp2 - tmp3)
z2 = sqrt(m2)

print("{0:.2f} {1:.4f}".format(m1, z1))
print()
print("{0:.2f} {1:.4f}".format(m2, z2))