import asyncio
from aiogram import Bot, Dispatcher 
from aiogram.types import Message


bot = Bot(token='xxx')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Hi')
    await message.reply('Hi, Bro')

async def main():
    await dp.start_polling(bot)
    
    if __name__== '__main__':
        asyncio.run(main())