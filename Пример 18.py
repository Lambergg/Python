#Расчёт по двум формулам
# 1. z1 = (a+2/sqrt(2a) - a/sqrt(2a)+2 + 2/a-sqrt(2a)) * sqrt(a)-sqrt(2)/a+2;
#При a1=4 z1=0.2928932; a1=21 z1=0.1667559; a1=11 z1=0.2113790; a1=7 z1=0.2463075; a1=5 z1=0.2739515;
# 2. z2 = 1/sqrt(a)+sqrt(2);
#При a2=2 z2=0.3535534; a2=11 z2=0.2113790; a2=6 z2=0.2588190; a2=10 z2=0.2185080; a2=24 z2=0.1583985;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
tmp = a1 + 2
tmp1 = sqrt(2 * a1)
tmp2 = tmp1 + 2
tmp3 = a1 - tmp1

z1 = ((tmp / tmp1) - (a1 / tmp2) + (2 / tmp3)) * ((sqrt(a1) - sqrt(2)) / tmp)
z2 = 1 / ((sqrt(a2)) + (sqrt(2)))

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))