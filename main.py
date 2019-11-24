import telebot
import requests
import horoscope
import anecdot
import say
import huiSlog
from telebot.types import Message

TOKEN = '700439547:AAF-WXbcpVnss30bKDRaBBQEi5q_FZcesQk'
urlTokenBot = f"https://api.telegram.org/bot{TOKEN}"
sendMessage = 'sendMessage'
getMe = 'getMe'
getUpdates = 'getUpdates'
notUnderstend = ' !!! я не знаю такой команды !!!'

r = requests.get(f'{urlTokenBot}/{getUpdates}')


def urlZapros(string):  # this method get url
    r = requests.get(f'{urlTokenBot}/{string}')
    print(r.json())


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я реогирую только на "привет"  "пока" "пошути"  и знак зодиака ')


@bot.message_handler(commands=['help'])
def start_message(message: Message):
    bot.send_message(message.chat.id, 'Извини я еще безполезен, но я учусь. Пока я понимаю "привет" "пока" ')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'privet':
        bot.reply_to(message, 'И тебе привет ))')

    elif message.text.lower() == 'пока' or message.text.lower() == 'poka':
        bot.send_message(message.chat.id, 'Покааа (')

    elif len(message.text.lower().split()) == 2 and message.text.lower().partition(' ')[
        0] == 'зодиак' and horoscope.validZnak(message.text.lower().partition(' ')[2]):
        bot.reply_to(message, horoscope.parse_html(horoscope.get_html(
            horoscope.urlHoroscope + horoscope.horoscopeZnak(message.text.lower().partition(' ')[2]))))

    elif message.text.lower() == 'расскажи анекдот' or message.text.lower() == 'мне скучно' or message.text.lower() == 'пошути':
        smeshno = anecdot.parse_html_anecdot(anecdot.get_html_anecdot(anecdot.urlAnecdot))
        bot.send_message(message.chat.id, smeshno)


    elif message.text.lower().partition(' ')[0] == 'воспроизведи:':
        print('воспроизвожу')
        chat_id = message.chat.id
        say.sayV(message.text.lower().partition(' ')[2])
        bot.send_voice(chat_id=chat_id, voice=open(r'C:\Users\tolchelnikov\telBot\1.ogg', 'rb'))


    else:
        bot.send_message(message.chat.id, huiSlog.huislog(message.text.lower()) + notUnderstend)


bot.polling(timeout=60)
