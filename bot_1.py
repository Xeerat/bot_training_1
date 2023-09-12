import telebot

TOKEN = '6464780141:AAEAqr-P1gFpG3o2mfcch8rq-qK-pBQo1Lo'

bot = telebot.TeleBot(TOKEN) # Создаю бота с определенным токеном

@bot.message_handler(content_types=['text']) # Эта функция реагирует на определенные события
 											 # В данном случае на любой текст от пользователя
 											 # Она действует на все функции ниже
 											 # До момента пока ты не пропишешь такую же функцию но на другое событие
def reverse_text(message): # message это большой массив с большим количество атрибутов
	reverse_message = reversed(message.text)
	print(str(reverse_message))
	bot.send_message(message.chat.id, reverse_message)

bot.polling(none_stop=True) # Эта функция не дает боту выключиться