import telebot

token = "8152166324:AAEFFn2vEqiDIyHlSEHVPbvlR5yLX-BcuBk"

bot = telebot.TeleBot(token)
import random

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

bot.polling(none_stop=True)