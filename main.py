import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN_TELEGRAM = "6325023349:AAHuQyWMjvFwbrndh6nHHDPs7AJrsev8zAY"
ADMIN_ID="869031863"

async def main():
    bot = Bot(token=TOKEN_TELEGRAM)
    dp = Dispatcher()
    dp.message.register(start_bot,F.text == "/start")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def start_bot(message: Message):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Здравствуйте, Администратор!")
    else:
        await message.answer("ОШИБКА! Доступ запрещен!", )




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)