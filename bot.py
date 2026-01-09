import telebot

token = "8366099038:AAHmc9YxHLtfhiXaEGkUmpphTd65lYCQvIk"

bot = telebot.TeleBot(token)

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

bot.polling(none_stop=True)