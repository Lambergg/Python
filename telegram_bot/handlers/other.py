from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#Фильтр от мата
#@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Мат запрещён!!!!!')
        await message.delete()  
   
def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)

#if message.text == 'Hi':
#       await message.reply('You are welcome friend!')
#   elif message.text == 'hi':
#       await message.reply('You are welcome bro!')
#  elif message.text == 'Privet':
#       await message.reply('Try to Russian')
#  elif message.text == 'privet':
#       await message.reply('Try to Russian!')
#    elif message.text == 'Привет':
#       await message.reply('Я научился русскому')
#   elif message.text == 'привет':
#       await message.reply('Я научился русскому за ночь :)') 

    # The bot forwards the user's message
    #await message.answer(message.text)

    # The bot responds to the user with his message
    #await message.reply(message.text)

    # The bot responds to the user in private messages and the group with his message
    #await bot.send_message(message.from_user.id, message.text)