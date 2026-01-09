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


@bot.message_handler(func=lambda message: True)
def say_hello(message):
    text = message.text.lower()
    if text == "Салам":
      bot.send_message(message.chat.id, "Салам кандайсын")
    elif text == "жакшы озун":
      bot.send_message(message.chat.id,"менда жакшы")
    elif text == "менде мындай суроо бар":
        bot.send_message(message.chat.id,"суроонузду бериниз")
    elif text == "дуйнодогу эн чон дарыя ":
        bot.send_message(message.chat.id,"дуйнодогу эн чон дарыя нил дарыясы")
    elif text == "id":
        bot.message_handler(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id,f"{message.text}")
