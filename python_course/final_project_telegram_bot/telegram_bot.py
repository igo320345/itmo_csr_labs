import telebot
from telebot import types
from jokes_parser import JokesParser
from dotenv import dotenv_values

bot = telebot.TeleBot(dotenv_values('.env')['API_KEY'])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Анекдот дня 😂'), types.KeyboardButton('Категории 📚'), types.KeyboardButton('Рандомный 🎲'))
    bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    jokes_parser = JokesParser()
    if message.text == 'Анекдот дня 😂':
        bot.send_message(message.chat.id, jokes_parser.get_joke_day())
    if message.text == 'Категории 📚':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), 
                   types.KeyboardButton('Вовочка 🤷‍♂'), 
                   types.KeyboardButton('Студенты 🤓'), 
                   types.KeyboardButton('Британские ученые 🧑‍🔬'),
                   types.KeyboardButton('Цитаты 💬'),
                   types.KeyboardButton('Программисты 🧑‍💻'), 
                   types.KeyboardButton('Вернуться в меню 🔙'))
        bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)
    if message.text == 'Рандомный 🎲':
        bot.send_message(message.chat.id, jokes_parser.get_random())  
    
    if message.text == 'Вернуться в меню 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Анекдот дня 😂'), types.KeyboardButton('Категории 📚'), types.KeyboardButton('Рандомный 🎲'))
        bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup)
    
    if message.text == 'Студенты 🤓':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Студенты 🤓'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('студент'), reply_markup=markup)
        

    if message.text == 'Спорт 💪':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('спорт'), reply_markup=markup)
    
    if message.text == 'Вовочка 🤷‍♂':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Вовочка 🤷‍♂'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('вовочка'), reply_markup=markup)
    
    if message.text == 'Британские ученые 🧑‍🔬':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Британские ученые 🧑‍🔬'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('британские%20ученые'), reply_markup=markup)
    
    if message.text == 'Цитаты 💬':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Цитаты 💬'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('цитаты'), reply_markup=markup)
    
    if message.text == 'Программисты 🧑‍💻':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Программисты 🧑‍💻'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, jokes_parser.get_topic_joke('программист'), reply_markup=markup)
    
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), 
                   types.KeyboardButton('Вовочка 🤷‍♂'), 
                   types.KeyboardButton('Студенты 🤓'), 
                   types.KeyboardButton('Британские ученые 🧑‍🔬'),
                   types.KeyboardButton('Цитаты 💬'),
                   types.KeyboardButton('Программисты 🧑‍💻'), 
                   types.KeyboardButton('Вернуться в меню 🔙'))
        bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

bot.polling()