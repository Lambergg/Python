#Расчёт по двум формулам
# 1. z1 = sin**4a+2sinacosa-cos**4a / tg2a-1;
#При a1=4 z1=-0.1455000; a1=2 z1=-0.6536436; a1=-1 z1=-0.4161468; a1=7 z1=0.1367372; a1=-5 z1=-0.8390715;
# 2. z2 = cos2a;
#При a2=2 z2=-0.6536436; a2=-1 z2=-0.4161468; a2=6 z2=0.8438540; a2=10 z2=0.4080821; a2=24 z2=-0.6401443;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
tmp = (sin(a1))**4
tmp1 = (2*(sin(a1)*cos(a1)))
tmp2 = (cos(a1))**4
tmp3 = (tan(2*a1))-1

z1 = (tmp+tmp1-tmp2) / tmp3
z2 = cos(2*a2)

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))