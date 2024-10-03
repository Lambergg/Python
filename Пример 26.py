#Расчёт по двум формулам
# 1. z1 = tg(x-pi/2)*cos(3pi/2+x)-sin**3(3.5pi-x) / cos(x-0.5pi)*tg(1.5pi+x);
#При x1=4 z1=0.5727500; x1=2 z1=0.8268218; x1=-1 z1=0.7080734; x1=7 z1=0.4316314; x1=-5 z1=0.9195358;
# 2. z2 = sin**2(x);
#При x2=2 z2=0.8268218; x2=-1 z2=0.7080734; x2=6 z2=0.0780730; x2=10 z2=0.2959590; x2=24 z2=0.8200722;

from math import *

x1 = float(input('Введите параметр x1 = '))
x2 = float(input('Введите параметр x2 = '))
tmp = tan(x1-(pi/2))
tmp1 = cos(((3*pi)/2)+x1)
tmp2 = (sin((3.5*pi)-x1))**3
tmp3 = cos(x1-(0.5*pi))
tmp4 = tan((1.5*pi)+x1)

z1 = (tmp*tmp1-tmp2) / (tmp3*tmp4)
z2 = (sin(x2))**2

print("{0:.2f} {1:.4f}".format(x1, z1))
print()
print("{0:.2f} {1:.4f}".format(x2, z2))