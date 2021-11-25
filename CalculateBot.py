import telebot
from telebot import types
TOKEN = '1851006243:AAGfe-Keo9cWFqMg13B69TqP-F5FcoixFFU'
bot = telebot.TeleBot(TOKEN,parse_mode='HTML')
KIRITISH1 = '<b>✏️Son kiriting:</b>'
KIRITISH2 = '<b>✏️Ikkinchi sonni kiriting:</b>'

@bot.message_handler(content_types=['text'])
def s(message):
    s = []
    s.append(message)
    bot.send_message(
        chat_id=message.chat.id,
        text='Ariza qabul qilindi'
    )
    print(message.text)


Num1 = {}
Num2 = {}
operator = {}
s = ['+', '-', '*', '/']

def plus(message):
    return eval(str(Num1[0])+operator[0]+str(Num2[0]))

def faction(message):
    if Num1[0] == 0:
        return 1
    return faction(Num1[0]-1)


def fes(message):
    s=1
    for i in range(1,Num1[0]+1):
        s*=i
    return s


def is_digit(message):
    try:
        a=int(message.text)
        return True
    except Exception:
        return False










@bot.message_handler(commands=['start'])
def start_message_handler(message):
    chat_id = message.chat.id
    text = '<b>Botni ishlatish uchun <i>/calculate</i>  tugmani  bosing</b>'
    bot.send_message(
        chat_id=chat_id,
        text=text

    )



@bot.message_handler(commands=['calculate'])
def text_message_handler(message):
    chat_id = message.chat.id
    message = bot.send_message(chat_id,KIRITISH1)
    bot.register_next_step_handler(message,number1_message_handler)

def number1_message_handler(message):
    try:
        a = int(message.text)
        Num1[0] = a
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        keyboard.add('^2', '!')
        keyboard.add('+', '-')
        keyboard.add('/', '*')
        text_operator = '🧮<code>Operatorni tanlang:</code>'
        bot.send_message(
            chat_id=message.chat.id,
            text=text_operator,
            reply_markup=keyboard

        )



    except:

         chat_id = message.chat.id
         text = '😏<code>Butun son kiriting:</code>'
         bot.send_message(chat_id,text)
         bot.register_next_step_handler(message,number1_message_handler)



@bot.message_handler(func = lambda message:message.text =='^2')
def kv_handler(message):
        bot.send_message(
            chat_id=message.chat.id,
            text=f'👌<b>Natija:{Num1[0]**2}</b>',


        )
        text_message_handler(message)

@bot.message_handler(func=lambda message:message.text=='!')
def factional_message_handler(message):
   bot.send_message(
        chat_id=message.chat.id,
        text=f'👌<b>Natija:</b>{fes(message)}'

    )

   text_message_handler(message)


@bot.message_handler(func=lambda message:message.text in s)
def operator_message_handler(message):
    chat_id = message.chat.id
    operator[0] = message.text
    message = bot.send_message(
        chat_id,
        text=KIRITISH2
        )
    bot.register_next_step_handler(message,number2_message_handler)
def number2_message_handler(message):
    if message.text == '0':
        bot.send_message(
            chat_id=message.chat.id,
            text='0 ga bo\'lish mumkin emas'
        )
        text_message_handler(message)

    else:

        try:
            b = int(message.text)
            Num2[0] = b
            bot.send_message(
                chat_id=message.chat.id,
                text=f'👌<b>Natija:</b>{plus(message)}'

            )
            text_message_handler(message)

        except:
            chat_id = message.chat.id
            text = '😏<code>Butun son kiriting:</code>'
            bot.send_message(chat_id,text)
            bot.register_next_step_handler(message,number2_message_handler)


bot.polling()