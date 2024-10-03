#Расчёт по двум формулам
# 1. z1 = sin**2(pi+a)+sin**2(pi/2+a)/cos(3pi/2+a) * ctg(1.5pi-a);
#При a1=4 z1=-1.5298857; a1=2 z1=-2.4029980; a1=-1 z1=1.8508157; a1=7 z1=1.3264319; a1=-5 z1=3.5253201;
# 2. z2 = 1/cosa;
#При a2=2 z2=-2.4029980; a2=-1 z2=1.8508157; a2=6 z2=1.0414819; a2=10 z2=-1.1917935; a2=24 z2=2.3574953;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
tmp = (sin(pi+a1))**2
tmp1 = (sin((pi/2)+a1))**2
tmp2 = (cos(((3*pi)/2)+a1))
tmp3 = 1/(tan((1.5*pi)-a1))

z1 = ((tmp+tmp1)/(tmp2)) * tmp3
z2 = 1 / cos(a2)

print("{0:.2f} {1:.4f}".format(a1, z1))
print()
print("{0:.2f} {1:.4f}".format(a2, z2))