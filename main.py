from sys import path
# Показываю папку из которой буду брать модули
path.insert(0, 'D://GitHub')
# Модуль из этого каталога
import bot_token

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = bot_token.TOKEN
bot = Bot(token = TOKEN)
# Является основным 'Секретарем'
dp = Dispatcher(bot)
# Будет что то делать когда в чате появятся данные команды
@dp.message_handler(commands=['start', 'help'])
# asyns def - особенность aiogram
async def send_welcome(msg: types.Message):
	# await - дождаться msg от пользователя
	# answer - просто ответ
	await msg.answer(
		f'Я бот. Приятно познакомиться {msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
	if msg.text.lower() == 'привет':
		await msg.answer('Привет!')
	else:
		# reply - ответ на определенное сообщение
		await msg.reply("Не понимаю что это значит.")

if __name__ == '__main__':
	# Запуск
	executor.start_polling(dp)