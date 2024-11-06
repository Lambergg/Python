from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start'])
async def commands_start(message : types.Message):
    try:
        await message.reply('Добро пожаловать на канал, рад вас всех видеть!!!', reply_markup=kb_client)
        #await bot.send_message(message.from_user.id,'Добро пожаловать на канал, рад вас всех видеть!!!', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Чтобы связаться с ботом напишите ему:\nhttps://t.me/MishaninaBot')

#@dp.message_handler(commands=['Общение'])
async def commands_social(message : types.Message):
    try:
        await message.reply('\nhttps://vk.com/ashashy , \nhttps://soundcloud.com/user-667203638 , \nhttps://vk.com/mmmmaaaarrrrtttt', reply_markup=kb_client)
        #await bot.send_message(message.from_user.id, '\nhttps://vk.com/ashashy , \nhttps://soundcloud.com/user-667203638 , \nhttps://vk.com/mmmmaaaarrrrtttt', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Чтобы связаться с ботом напишите ему:\nhttps://t.me/MishaninaBot')


#@dp.message_handler(commands=['Youtube'])
async def commands_youtube(message : types.Message):
    try:
        await message.reply('\nhttps://www.youtube.com/channel/UCMiuPxn50PwUd6EW_7Ul1JA', reply_markup=kb_client)
        #await bot.send_message(message.from_user.id, '\nhttps://www.youtube.com/channel/UCMiuPxn50PwUd6EW_7Ul1JA', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Чтобы связаться с ботом напишите ему:\nhttps://t.me/MishaninaBot')

#@dp.message_handler(commands=['Почта'])
async def commands_email(message : types.Message):
    try:
        await message.reply('\nashymane@vk.com', reply_markup=ReplyKeyboardRemove())
        #reply_markup=ReplyKeyboardRemove() убрать клавиатуру
        #await bot.send_message(message.from_user.id, '\nashymane@vk.com', reply_markup=ReplyKeyboardRemove())
        #await message.delete()
    except:
        await message.reply('Чтобы связаться с ботом напишите ему:\nhttps://t.me/MishaninaBot')

        ##################################################################################################
def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start'])
	dp.register_message_handler(commands_social, commands=['Общение'])
	dp.register_message_handler(commands_youtube, commands=['Youtube'])
	dp.register_message_handler(commands_email, commands=['Почта'])        