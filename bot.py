import json

import asyncio
import requests

from aiogram import Bot, Dispatcher, types

from config import bot_token

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добрый день.\n\n прикрепите AINSYS Вебхук.")


@dp.message_handler(content_types="text")
async def extract_data(message: types.Message):
    print(message.text)
    chat_info = message.chat
    if 'https' in message.text:
        data = {
            'webhook': message.text,
            'chat_id': chat_info['id'],
            'action': 'get_webhook'
        }
        webhook = requests.post("http://127.0.0.1:5000/webhook", data=json.dumps(data),
                                headers={"Content-Type": "application/json"})


        await message.answer(f"Ваш вебхук: {webhook.text}")
        await message.answer(f"Инструкция по использованию бота. Вы можете \n\n - Создать сущность /add_entity \n "
                             f"- Показать все сущности\n")

    if message.text == '/add_entity':
        await message.answer(f"Введите название вашей сущности в формате, например - \n"
                             f"Сущность: New")

    if "Сущность" in message.text:

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Создать сущность", callback_data="add_entity"))

        await message.answer(f"Введите название вашего поля и тип данных в формате, например - \n\n"
                             f"Поле: Имя \n"
                             f"Тип: string \n\n"
                             f"Если вам нужно еще ввести поле, введите в таком же формате, если нет"
                             f"Нажмите на кнопку 'Создать сущность'", reply_markup=keyboard)


@dp.callback_query_handler(text="add_entity")
async def send_random_value(call: types.CallbackQuery):
    data = {
        'action': 'add_entity',
    }
    success_answer = requests.post("http://127.0.0.1:5000/webhook", data=json.dumps(data),
                            headers={"Content-Type": "application/json"})
    
    await call.message.answer(str(success_answer.text))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
