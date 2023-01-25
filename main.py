import aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove  # Импртируем классы для создания клавиатуры
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from keybords import ikb
import asyncio
from aiogram.utils.exceptions import BotBlocked #Ипортируем для проверки заблокирован ли бот


# бот это сервер который будет взаимодействовать с API Telegram

TOKEN_API  # авторизационный токен для подключения к телеграм API перенесен в отдельный файл config.py
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
