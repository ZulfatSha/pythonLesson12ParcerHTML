from bs4 import BeautifulSoup
import requests

url = 'https://lenta.ru/parts/news/'


response = requests.get(url)

# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.a)
#
# print(soup.a.string)
#
# print(soup.a.get('href'))

data = soup.find_all('li', class_='parts-page__item')

# Последним в списке элементов использован "показать еще", надо убрать:
data.pop()


for i in data:
    news = i.find('h3', class_= 'card-full-news__title').text
    link = 'https://lenta.ru/parts' + i.find('a', class_= 'card-full-news _parts-news').get('href')
    time = i.find('time', class_= 'card-full-news__info-item card-full-news__date').text

    print('Новость: ' + news)
    print('Ссылка: ' + link)
    print('Время: ' + time)