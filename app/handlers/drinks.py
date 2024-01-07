from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


drinks = ["кофе", "чай", "кумыс"]
drinks_size = ["маленький", "средний", "большой"]

class OrderDrink(StatesGroup):
	waiting_for_drink_name = State()
	waiting_for_drink_size = State()

async def drink_start(message: types.Message, state: FSMContext):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	for name in drinks:
		keyboard.add(name)
	await message.answer("Выберите напиток:", reply_markup=keyboard)
	await state.set_state(OrderDrink.waiting_for_drink_name.state)

async def drink_chosen(message: types.Message, state: FSMContext):
	if message.text.lower() not in drinks:
		await message.answer("Пожалуйста выберите напиток, используя клавиатуру ниже.")
		return
	await state.update_data(chosen_drink=message.text.lower())
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	for name in drinks_size:
		keyboard.add(name)
	await message.answer("Хорошо, теперь выберите размер напитка:", reply_markup=keyboard)
	await state.set_state(OrderDrink.waiting_for_drink_size.state)

async def drink_size_chosen(message: types.Message, state: FSMContext):
	if message.text.lower() not in drinks_size:
		await message.answer("Пожалуйста выберите размер напитка, используя клавитуру ниже.")
		return
	user_data = await state.get_data()
	await message.answer(f"Вы заказали {message.text.lower()} {user_data['chosen_drink']}.\n"
				f"Спасибо за заказ!", reply_markup=types.ReplyKeyboardRemove())
	await state.finish()		

def register_handlers_drinks(dp: Dispatcher):
	dp.register_message_handler(drink_start, commands='drinks', state='*')
	dp.register_message_handler(drink_chosen, state=OrderDrink.waiting_for_drink_name)
	dp.register_message_handler(drink_size_chosen, state=OrderDrink.waiting_for_drink_size)