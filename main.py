from asyncio import run
from logging import getLogger, basicConfig, INFO

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.handlers.drinks import register_handlers_drinks
from app.handlers.food import register_handlers_food
from app.handlers.common import register_handlers_common

logger = getLogger(__name__)

async def set_commands(bot: Bot):
	commands = [
		BotCommand(command="/drinks", description="Заказать напитки"),
		BotCommand(command="/cancel", description="Отменить текущее действие"),
		BotCommand(command="/food", description="Заказать блюда")
	]
	await bot.set_my_commands(commands)

async def main():
	basicConfig(level=INFO,
		format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
	)
	logger.error("Starting bot")

	bot = Bot(token='6464780141:AAEAqr-P1gFpG3o2mfcch8rq-qK-pBQo1Lo')
	dp = Dispatcher(bot, storage=MemoryStorage())

	register_handlers_common(dp)
	register_handlers_drinks(dp)
	register_handlers_food(dp)

	await set_commands(bot)

	await dp.start_polling()

if __name__ == '__main__':
	run(main())