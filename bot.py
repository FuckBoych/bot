import telebot

STICKER_ID = 'CAACAgIAAxkBAAOCXnYT0q1uI3UqMtX3G4qrFLHT_rQAAo8BAAIf9rYbVUDpcOToXHUYBA'
bot = telebot.TeleBot('1114578839:AAGgL9ihU5csiN0ti0xse22deNEAQ87Syys')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, бродяга. Я творение Святого Матвея. Я отвечаю на все стикером, так что да, функционал у меня еще не готов. Но я уверен что создатель что-то придусает )))')

@bot.message_handler(content_types=['text'])
def sticker(message):
	bot.send_sticker(message.chat.id, STICKER_ID)

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	bot.send_message(message.chat.id, 'Норм')
	
	
@bot.message_handler(content_types=['sticker'])
def sticker(message):
	bot.send_sticker(message.chat.id, STICKER_ID)
	#print (message.sticker)
bot.polling()
