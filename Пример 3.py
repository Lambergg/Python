#Стоимость содержания автомобиля
service = float(input('Стоимость ТО: '))
fuel = float(input('Стоимость топлива: '))
tax = float(input('Транспортный налог: '))
tuning = float(input('Тюнинг и прочие доработки: '))
insurance = float(input('ОСАГО: '))

total = service + fuel + tax + tuning + insurance
print('Всего: ', total)
