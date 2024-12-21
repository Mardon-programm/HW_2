from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command 
from config import token
import asyncio
from button import  MENU, genrate_menu_keyboard

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Здравствуйте уважаемый пользователь.")

@dp.message(Command('help'))
async def help(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer(
        "Доступные команды:\n\n"
        "/start - Начать взаимодействие с ботом\n"
        "/about - Короткая информация про бота\n"
        "/help - Получить помощь\n"
        "/menu - Повторить меню\n\n",
        reply_markup=keyboard
    )


@dp.message(Command('about'))
async def about(message:types.Message):
    await message.answer("Этот бот предоставляет пользователям информацию по различным запросам. "
        "Он может показать новости, курсы валют, контактную информацию и FAQ.")
        
@dp.message(Command("menu"))
async def menu_message(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer("Выберите тему из меню:", reply_markup=keyboard)

@dp.message(F.text == "Новости")
async def send_news(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer("Сегодня: курс доллара вырос на 2%, акции падают.", reply_markup=keyboard)

@dp.message(F.text == "Курсы валют")
async def send_exchange_rates(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer("Доллар: 85₽, Евро: 90₽.", reply_markup=keyboard)

@dp.message(F.text=="Контактная информация")
async def send_contacts(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer("Наша почта: info@example.com. Телефон: +123456789.", reply_markup=keyboard)

@dp.message(F.text == "Часто задаваемые вопросы - FAQ")
async def send_faq(message: types.Message):
    keyboard = genrate_menu_keyboard()
    await message.answer(
        "1. Как получить информацию? - Выберите тему из меню.\n"
        "2. Как связаться с поддержкой? - Напишите на почту info@example.com.", reply_markup=keyboard
    )

@dp.message()
async def handle_other_messages(message: types.Message):
    await message.answer("Я не понял вашего сообщения. Могу помочь вам с командой /help.")


async def main():
    print("Запукс Бота")
    await dp.start_polling(bot)

asyncio.run(main())