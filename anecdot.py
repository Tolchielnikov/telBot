import requests
import urllib.request
from bs4 import BeautifulSoup

urlAnecdot = 'http://anekdotme.ru/random'

r = requests.get(urlAnecdot)


def get_html_anecdot(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse_html_anecdot(html):
    soup = BeautifulSoup(html)
    table = soup.find('div', 'anekdot_text').text
    return table


print(parse_html_anecdot(get_html_anecdot(urlAnecdot)))
