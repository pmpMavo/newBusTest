import telebot
from telebot import types
import requests

bot = telebot.TeleBot('5695501523:AAECzCId78HvjdGwArB6on853ovk1eVXbYE')

@bot.message_handler(commands=['start'])
def get_start(message):
    get_start = types.InlineKeyboardMarkup()
    key_start = types.InlineKeyboardButton(text='Старт', callback_data='start')

    get_start.add(key_start)
    welcome_text = 'Привет! Для старта работы нажми "Старт"'
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_start)

@bot.callback_query_handler(func=lambda m:True)
def start_is_ok(call):
    if call.data == 'start':
        bot.send_message(call.message.chat.id, 'Бот успешно запущен!')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_bus_stop = types.KeyboardButton(text='Выбрать остановку')
    key_time = types.KeyboardButton(text='За сколько уведомлять до прибытия автобуса?')

    keyboard.add(key_bus_stop, key_time)

    if call.data == 'five':
        bot.send_message(call.message.chat.id, 'Вы будете уведомлены за 5 минут до приезда автобуса')
    elif call.data == 'ten':
        bot.send_message(call.message.chat.id, 'Вы будете уведомлены за 10 минут до приезда автобуса')
    elif call.data == 'fifteen':
        bot.send_message(call.message.chat.id, 'Вы будете уведомлены за 15 минут до приезда автобуса')


@bot.message_handler(content_types=['text'])
def set_time(message):
    if message.text == 'За сколько уведомлять до прибытия автобуса?':
        set_time_inline = types.InlineKeyboardMarkup()
        five_min = types.InlineKeyboardButton(text='За 5', callback_data='five')
        ten_min = types.InlineKeyboardButton(text='За 10', callback_data='ten')
        fifteen_min = types.InlineKeyboardButton(text='За 15', callback_data='fifteen')

        text_pick_time = 'Выберите за сколько минут до прибытия автобуса вам будет приходить уведомление'
        set_time_inline.add(five_min, ten_min, fifteen_min)
        bot.send_message(message.chat.id, text_pick_time, reply_markup=set_time_inline)



bot.polling(none_stop=True, interval=0)