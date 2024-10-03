#Пример из лабораторной работы №1
#Найти y функции

from math import * # Теперь можно так print sin(pi/4)

x = float(input('Введите значение x: '))

if x < -5:
    y = 1

elif x >= -5 and x < 0:
    y = (3 / 5) * x - 2

elif x >= 0 and x < 2:
    y = -sqrt(4 - x ** 2)

elif x >= 2 and x < 4:
    y = x - 2

elif x >= 4 and x < 8:
    y = 2 + sqrt(4 - (x - 6) ** 2)

else:
    y = 2

print("X = {0:.2f} Y = {1:.2f}".format(x,y))