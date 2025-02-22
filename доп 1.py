#Запрос кол-ва пингвинов у пользователя:
n=int(input('Введите кол-во пенгвинов от 1 до 9: '))

#Пингвин:
head = "   _~_     "
eyes = "  (o o)    "
body = " /  V  \\   "
legs = "/(  _  )\\  "
foot = "  ^^ ^^    "

#Вывод пенгвинов:
print(n * head)
print(n * eyes)
print(n * body)
print(n * legs)
print(n * foot)
