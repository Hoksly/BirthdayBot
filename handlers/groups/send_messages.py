from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Message
from loader import dp
from data.config import ADMINS
from utils.misc.send_birtday_message import main_process, send_month_message
from data.globals import main_thread
counter = 0


@dp.message_handler(Command('start_sending'))
async def send_messages(message: types.Message):
    global counter
    print("HERE", message.chat.id)
    # print(ADMINS)
    counter += 1
    print(message.text)

    await main_process()




@dp.message_handler(Command('a'))
async def send_month_message(message: types.message):
    #print(message.chat.id)
    print(message.text)
    #await send_month_message()

'''
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def send_s_th(message: types.Message):
    print(message.chat.id)
    print(message.text)
'''