#Вычисление времени в пути
dist = 0 #Расстояние
speed = 0 #Скорость

dist = int(input('Расстояние:' ))
speed = int(input('Планируемая средняя скорость:'))

time = dist * 60 / speed

print('Время в пути ',time, 'Минут')