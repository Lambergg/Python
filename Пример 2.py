#Вычисление расхода топлива
consum = 0 #Средний расход 10.5л/100км
dist = 0 #Расстояние, км

consum = float(input('Средний расход топлива л/100км: '))
dist = float(input('Расстояние, км: '))
result = consum * dist / 100
print('Необходимо: ',result , 'л.')
