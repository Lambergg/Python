#Пример из лабораторной работы №2
#Попадает ли точка в заштрихованную область

from math import *

flag = 0

print('Введите координаты точки')

x = float(input('X = '))

y = float(input('Y = '))

if (x < -1) or (x > 4):
    flag = 0 #False

if (x >= -1) and (x < 1) and (y >= 2 * x+2) \
    and (x <= x ** 3 - 4 * x ** 2 + x + 6) \
    and (y <= 2 * x + 2):
    flag =1

else:
    flag =0

print("Точка X = {0: 6.2f} Y = {1: 6.2f}" \
      .format(x ,y), end=' ')

if flag:
    print('Попадает в область')

else:
    print('Не попадает в область')