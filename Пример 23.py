#Расчёт по двум формулам
# 1. z1 = (1+6ac/a**3-8c**3 - 1/a-2c) / (1/a**3-8c**3 - 1/a**2+2ac+4c**2);
#При a1=4 c1=1 z1=3.0; a1=2 c1=-1 z1=5.0; a1=-1 c1=6 z1=-12.0; a1=7 c1=10 z1=-12.0; a1=-5 c1=24 z1=-52.0;
# 2. z2 = 1-2c+a;
#При a2=2 c2=4 z2=-5.0; a2=-1 c2=2  z2=-4.0; a2=6 c2=-1 z2=9.0; a2=10 c2=7 z2=-3.0; a2=24 c2=-5 z2=35.0;

from math import *

a1 = float(input('Введите параметр a1 = '))
c1 = float(input('Введите параметр c1 = '))
a2 = float(input('Введите параметр a2 = '))
c2 = float(input('Введите параметр c2 = '))
tmp = 1+(6*(a1*c1))
tmp1 = ((a1**3) - (8*(c1**3)))
tmp2 = (1/(a1-(2*c1)))
tmp3 = (1/((a1**3)-(8*(c1**3))))
tmp4 = (1/((a1**2)+(2*(a1*c1))+(4*(c1**2))))

z1 = ((tmp/tmp1) - (tmp2)) / (tmp3 - tmp4)
z2 = 1 - (2*c2) + a2

print("{0:.2f} {1:.2f} {2:.4f}".format(a1, c1, z1))
print()
print("{0:.2f} {1:.2f} {2:.4f}".format(a2, c2, z2))