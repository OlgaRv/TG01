import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://i.pinimg.com/736x/ed/b8/e1/edb8e13206ed9e5a633e16f2d27be783.jpg',
            'https://clipart-library.com/2023/856-8565648_lavender-clipart-rosemary-plant-anemone-flower-png.png',
            'https://i.ytimg.com/vi/_zD_uPj5VhE/maxresdefault.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Спасибо за фото')
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какое фото', 'Непонятно что это такое', 'Не отправляй мне это больше']
    rand_answer = random.choice(list)
    await message.answer(rand_answer)
@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Иску́сственный интелле́кт (ИИ; искин; англ. artificial intelligence, AI) '
                         '— свойство искусственных интеллектуальных систем выполнять творческие функции, '
                         'которые традиционно считаются прерогативой человека[1] (не следует путать с искусственным сознанием); '
                         'наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ.')

@dp.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n/start \n/help')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!  Я бот!')

async def main(dp):
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main(dp))сч