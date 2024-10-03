#Расчёт по двум формулам
# 1. z1 = sqrt(1-sin(pi/2-a)/2) + sqrt(1+cos(2pi-a)/2) if pi<a<3pi/2 ;
#При a1=4 z1=1.3254443; a1=3.5 z1=1.1622320; a1=4.2 z1=1.3680555; a1=3.7 z1=1.2368654; a1=4.5 z1=1.4062468;
# 2. z2 = sin(a/2)-cos(a/2) if pi<a<3pi/2;
#При a2=2 z2=3011687; a2=-1 z2=-1.3570081; a2=2.6 z2=0.6960594; a2=2.1 z2=0.3698522; a2=2.4 z2=0.5696813;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
tmp = sin(pi/2 - a1)
tmp1 = cos(2*pi - a1)
tmp2 = ((3*pi) / 2)

if a1 > pi and a1 < tmp2:
    z1 = sqrt((1 - tmp) / 2) + sqrt((1 + tmp1) / 2)

if a1 > pi and a1 < tmp2:
    z2 = (sin(a2/2)) - (cos(a2/2))

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))