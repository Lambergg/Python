#Расчёт по двум формулам
# 1. z1 = a*sqrt(logab)-b*sqrt(logba)+tg(ab+3pi/2);
#При a1=4 b1=2 z1=0.1470651; a1=2 b1=11 z1=-115.1674233; a1=11 b1=3 z1=3.0267329; a1=7 b1=2 z1=0.6887503; a1=5 b1=10 z1=1.2979165;
# 2. z2 = tg(ab+3/2pi);
#При a2=2 b2=4 z2=0.1470651; a2=1 b2=3 z2=7.0152526; a2=6 b2=4 z2=0.4684067; a2=10 b2=8 z2=-0.1110660; a2=24 b2=12 z2=0.6052518;

from math import *

a1 = float(input('Введите параметр a1 = '))
a2 = float(input('Введите параметр a2 = '))
b1 = float(input('Введите параметр b1 = '))
b2 = float(input('Введите параметр b2 = '))
log_1 = sqrt(log(b1,a1))
log_2 = sqrt(log(a1,b1))
tmp = a1*log_1
tmp1 = b1*log_2
tmp2 = tan((a1*b1)+((3*pi)/2))

z1 = tmp-tmp1+tmp2
z2 = tan((a2*b2)+((3/2)*pi))

print("{0:.2f} {1:.2f} {2:.4f}".format(a1, b1, z1))
print()
print("{0:.2f} {1:.2f} {2:.4f}".format(a2, b2, z2))