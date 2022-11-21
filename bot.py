import asyncio

from aiogram import Bot, Dispatcher, types

from database.db_api import add_user, add_entity, get_entity_id, get_entities, add_field, get_fields_for_bot
from bot_worker import get_webhook, add_entity_ainsys, update_entity_ainsys
from config import bot_token
from constants import *

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=[BotCommand.START])
async def cmd_start(message: types.Message):
    await message.answer(BotMessage.START)


@dp.message_handler(commands=[BotCommand.HELP])
async def cmd_start(message: types.Message):
    await message.answer(BotMessage.HELP)


@dp.message_handler(commands=[BotCommand.ADD_ENTITY])
async def cmd_add_entities(message: types.Message):
    await message.answer(BotMessage.ADD_ENTITY_INSTRUCTION)


@dp.message_handler(commands=[BotCommand.GET_ENTITIES])
async def cmd_get_entities(message: types.Message):
    entities = get_entities(message.from_user.id)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*entities)

    await message.answer(BotMessage.USER + str(message.from_user.id))
    await message.answer(BotMessage.ENTITIES)
    await message.answer(str(entities))
    await message.answer(BotMessage.CHOOSE_ENTITY, reply_markup=keyboard)


@dp.message_handler(commands=[BotCommand.UPDATE_DATA])
async def cmd_get_entities(message: types.Message):
    entities = get_entities(message.from_user.id)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*entities)

    await message.answer(BotMessage.CHOOSE_ENTITY, reply_markup=keyboard)


@dp.message_handler(content_types=BotContentTypes.TEXT)
async def extract_data(message: types.Message):
    chat_info = message.chat
    user_id = message.from_user.id
    entities = get_entities(message.from_user.id)
    field = ''
    print(field)

    if ParcePhrase.FORMAT_URL in message.text:
        webhook = get_webhook(message.text, chat_info['id'])
        add_user(user_id, chat_info['id'], message.text)

        await message.answer(BotMessage.WEBHOOK + webhook.text)
        await message.answer(BotMessage.MAIN_INSTRUCTION)

    if ParcePhrase.ENTITY in message.text:
        entity_name = message.text[10:]
        add_entity(entity_name, user_id, chat_info['id'])
        entity_id = get_entity_id(entity_name)

        await message.answer(BotMessage.ID_ENTITY + str(entity_id))
        await message.answer(BotMessage.ADD_FIELD_INSTRUCTION)

    if ParcePhrase.FIELD in message.text:
        message_text = message.text
        info_for_field = message_text.split()
        info_for_field.remove(BotMessage.ID_ENTITY)
        info_for_field.remove(BotMessage.FIELD)
        info_for_field.remove(BotMessage.TYPE)

        entity_id, field, type_field = info_for_field
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(types.KeyboardButton(text=ButtonCommand.ADD_ENTITY + entity_id))

        add_field(entity_id, field, type_field, chat_info['id'], user_id)

        await message.answer(BotMessage.ADD_FIELD_INSTRUCTION_SECOND, reply_markup=keyboard)

    if ParcePhrase.CREATE_ENTITY in message.text:
        success_answer = add_entity_ainsys(user_id, message.text[20:], chat_info['id'])
        entities = get_entities(message.from_user.id)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*entities)

        await message.answer(str(success_answer.text))
        await message.answer(BotMessage.CHOOSE_ENTITY, reply_markup=keyboard)

    if message.text in entities:
        fields = get_fields_for_bot(message.text)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*fields)

        await message.answer(BotMessage.FIELDS, reply_markup=keyboard)

    if BotMessage.FIELD_AINSYS in message.text:  # в разработке, нужно продумать сбор данных
        field = message.text

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text=ButtonCommand.ADD_FIELDS))

        await message.answer(BotMessage.FIELDS_END, reply_markup=keyboard)

    if ButtonCommand.ADD_FIELDS == message.text:  # в разработке, нужно продумать сбор данных

        await message.answer(success_answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
