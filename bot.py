import telebot

token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text= f'Салам! {message.from_user.first_name}'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,'Бул бот томонку командаларды кыла алат:\n/start -Салам'
                                     '\n/help-жардам\n/menu-Reply меню\n/inline-Inline меню')
bot.polling(non_stop=True)
