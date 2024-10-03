#Расчёт по двум формулам
# 1. z1 = (m-1)*sqrt(m) - (n-1)*sqrt(n) / sqrt(m**3 * n) + n*m + m**2 - m;
#При m1=4 n1=2 z1=0.1464466; m1=2 n1=4 z1=-0.2928932; m1=11 n1=2 z1=0.1729465; m1=7 n1=5 z1=0.0585262; m1=5 n1=3 z1=0.1008034;
# 2. z2 = sqrt(m) - sqrt(n) / m;
#При m2=2 n2=4  z2=-0.2928932; m2=11 n2=3 z2=0.1440522; m2=6 n2=7 z2=-0.0327103; m2=10 n2=8 z2=0.0333851; m2=24 n2=9 z2=0.0791241;

from math import *

m1 = float(input('Введите параметр m1 = '))
n1 = float(input('Введите параметр n1 = '))
m2 = float(input('Введите параметр m2 = '))
n2 = float(input('Введите параметр n2 = '))
tmp = m1 - 1
tmp1 = n1 - 1
tmp2 = m1 ** 3
tmp3 = m1 ** 2

z1 = ((tmp * sqrt(m1)) - ((tmp1 * sqrt(n1)))) / ((sqrt(tmp2 * n1)) + (n1 * m1) + (tmp3 - m1))
z2 = ((sqrt(m2) - sqrt(n2))) / m2

print("{0:.2f} {1:.2f} {2:.4f}".format(m1, n1, z1))
print()
print("{0:.2f} {1:.2f} {2:.4f}".format(m2, n2, z2))