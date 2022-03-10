import telebot
from telebot import types

# main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

btn10 = types.KeyboardButton("Социальные сети")


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Получить первый видео урок")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text='Привествую вас! Вы сделали важный шаг к избавлению отлишнего веса - зашли сюда. Здесь вас ждут бесплатные видео уроки, из которых вы узнаете много полезного. Если вы готовы начать просмотр - нажмите "Получить видео урок"'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Получить первый видео урок"):
        markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Получить второй видео урок")
        markup_2.add(btn2)
        bot.send_message(message.chat.id, text="Ваш первый видео урок: Почему так сложно похудеть?\nhttps://youtu.be/9i-lt9khuFU", reply_markup=markup_2)
    elif (message.text == "Получить второй видео урок"):
        markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Получить третий видео урок")
        markup_3.add(btn3)
        bot.send_message(message.chat.id, text="Ваш второй видео урок: Почему кардио бесполезно?\nhttps://youtu.be/EIcUOn6F1a", reply_markup=markup_3)
    elif (message.text == "Получить третий видео урок"):
        markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Узнать больше")
        markup_4.add(btn4)

        bot.send_message(message.chat.id,text="Ваш третий видео урок: Диетические продукты для набора лишнего веса.\nhttps://youtu.be/niexOLzQjTE", reply_markup=markup_4 )
    elif (message.text == "Узнать больше"):
        markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_5 = types.InlineKeyboardMarkup()
        btn_site = types.InlineKeyboardButton(text="Подробная информация",
                                              url="https://taplink.cc/mikhail_spektor_/p/77e522/")
        markup_4.add(btn10)
        markup_5.add(btn_site)

        bot.send_message(message.chat.id,
                         text="Если вам интерсно узнать больше про избавление от лишнего веса, приглаглашаю вас постеить сайт моей Жиротопки Reboot - самой легкой в мире системы избавления от лишнего веса:\nhttps://taplink.cc/mikhail_spektor_/p/77e522/",
                         reply_markup=markup_5)
        bot.send_message(message.chat.id, text="Перейдите по ссылке выше или нажмите кнопку Подробная информация",
                         reply_markup=markup_4)
    elif (message.text == "Социальные сети"):
        markup_5 = types.InlineKeyboardMarkup()
        btn_con = types.InlineKeyboardButton(text="Instagram",
                                              url="https://www.instagram.com/mikhail_spektor_/")
        markup_5.add(btn_con)

        bot.send_message(message.chat.id, text="Как найти?",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,text="Ссылки на социальные сети",
                         reply_markup=markup_5)



while True:
    try:
        bot.polling()
    except:
        continue
