from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Start')
b2 = KeyboardButton('/Общение')
b3 = KeyboardButton('/Youtube')
b4 = KeyboardButton('/Почта')
b5 = KeyboardButton('Мой номер', request_contact=True) #Работает если написать непосредственно боту
b6 = KeyboardButton('Моя локация', request_location=True) #Работат если написать непосредственно боту

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).insert(b4).insert(b5).insert(b6)

# Метод add(b1) добавлет кнопку в виде строк друг под другом
# Метод insert(b2) добавляет кнопки справа от предыдущей в одной строке
# Метод row(b1, b2, b3, b4) добавляет кнопки друг за другом в строку
# one_time_keyboard=True одноразовость клавиатуры