import telebot
import random


token = ""
bot = telebot.TeleBot(token)

jokes = [
    "Программисттер кофе ичпесе, алар да error чыгарат 😄",
    "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 = Dec 25 🎃🎄",
    "Debugging — ошол убакыт, качан код иштейт, бирок сен эмне кылганыңды түшүнбөйсүң 🤯",
    "Почему компьютер холодный? Потому что он работает в Windows 🪟💻",
    "Stack Overflow'у колдобосоң — Python'до жоголосуң 🐍"
]
@bot.message_handler(commands=['joke'])
def send_joke(message):
    random_joke = random.choice(jokes)
    bot.send_message(message.chat.id, random_joke)




@bot.message_handler(commands=['start'])
def send_welcome(message):
    text= f'Салам! {message.from_user.first_name}'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,'Бул бот томонку командаларды кыла алат:\n/start -Салам'
                                     '\n/help-жардам\n/menu-Reply меню\n/inline-Inline меню')



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