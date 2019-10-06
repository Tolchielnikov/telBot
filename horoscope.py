import requests
import urllib.request
from bs4 import BeautifulSoup

urlHoroscope = 'http://1001goroskop.ru/?znak='
strelec = 'sagittarius'
oven = 'aries'
telec = 'taurus'
blizneci = 'gemini'
rak = 'cancer'
lev = 'leo'
deva = 'virgo'
vesi = 'libra'
scorp = 'scorpio'
cozerog = 'capricorn'
vodolei = 'aquarius'
ribi = 'pisces'

r = requests.get(urlHoroscope)


def horoscopeZnak(znak):
    if znak == 'Стрелец' or znak == 'стрелец':
        return strelec
    elif znak == 'Рак' or znak == 'рак':
        return rak
    elif znak == 'Овен' or znak == 'овен':
        return oven
    elif znak == 'Телец' or znak == 'телец':
        return telec
    elif znak == 'Близнецы' or znak == 'близнецы':
        return blizneci
    elif znak == 'Лев' or znak == 'лев':
        return lev
    elif znak == 'Дева' or znak == 'дева':
        return deva
    elif znak == 'Весы' or znak == 'весы':
        return vesi
    elif znak == 'Скорпион' or znak == 'скорпион':
        return scorp
    elif znak == 'Козерог' or znak == 'козерог':
        return cozerog
    elif znak == 'Водолей' or znak == 'водолей':
        return vodolei
    elif znak == 'Рыбы' or znak == 'рыбы':
        return ribi


def validZnak(znak):
    if znak == 'Стрелец' or znak == 'стрелец':
        return True
    elif znak == 'Рак' or znak == 'рак':
        return True
    elif znak == 'Овен' or znak == 'овен':
        return True
    elif znak == 'Телец' or znak == 'телец':
        return True
    elif znak == 'Близнецы' or znak == 'близнецы':
        return True
    elif znak == 'Лев' or znak == 'лев':
        return True
    elif znak == 'Дева' or znak == 'дева':
        return True
    elif znak == 'Весы' or znak == 'весы':
        return True
    elif znak == 'Скорпион' or znak == 'скорпион':
        return True
    elif znak == 'Козерог' or znak == 'козерог':
        return True
    elif znak == 'Водолей' or znak == 'водолей':
        return True
    elif znak == 'Рыбы' or znak == 'рыбы':
        return True
    else:
        return False


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse_html(html):
    soup = BeautifulSoup(html)
    table = soup.find('p')
    return table
