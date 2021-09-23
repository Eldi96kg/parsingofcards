import requests
from bs4 import BeautifulSoup
import csv

HOST='https://minfin.com.ua/'
URL='https://minfin.com.ua/cards/'
HEADERS={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}

def get_html(url,params=''):
    r=requests.get(url,headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='bfjox4-0 frZdag')
    cards = []
    for item in items:
        cards.append(
            {
                'title':item.find('a',class_='sc-6nr3q5-0 iyqRre').get_text(strip=True),# strip=True убрать пробелы
                'product_link': HOST+item.find('a', class_='sc-6nr3q5-0 iyqRre').get('href'),
                'brand': item.find('span', class_='bfjox4-20 jtOFL').get_text(strip=True),
                'card_img': item.find('a', class_='sc-6nr3q5-0 gpMICG').find('img').get('src'),

            }
        )
    return cards

def parser():
    pass



html = get_html(URL)
cards = get_content(html.text)
for i in cards:
    print(i)