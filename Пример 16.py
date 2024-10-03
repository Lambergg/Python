#Расчёт по двум формулам
# 1. z1 = x**2 + 2x - 3 + (x + 1) * sqrt(x**2 - 9) / x**2 - 2x - 3 + (x -1) * sqrt(x**2 - 9);
#При x1=4 z1=2.6457513; x1=7 z1=1.5811388; x1=9 z1=1.4142136; x1=8 z1=1.4832397; x1=12 z1=1.2909944;
# 2. z2 = sqrt(x + 3 / x - 3);
#При x2=8 z2=1.4832397; x2=5 z2=2.0000000; x2=6 z2=1.7320508; x2=10 z2=1.3627703; x2=24 z2=1.1338934;

from math import *

x1 = float(input('Введите параметр x1 = '))
x2 = float(input('Введите параметр x2 = '))
tmp = ((x2 + 3) / (x2 - 3))
tmp1 = x1 ** 2
tmp2 = 2 * x1
tmp3 = x1 + 1
tmp4 = x1 - 1

z1 = (tmp1 + tmp2 - 3 + tmp3 * sqrt(tmp1 - 9)) / (tmp1 - tmp2 - 3 + tmp4 * sqrt(tmp1 - 9))
z2 = sqrt(tmp)

print("{0:.2f} {1:.4f}".format(x1, z1))
print()
print("{0:.2f} {1:.4f}".format(x2, z2))