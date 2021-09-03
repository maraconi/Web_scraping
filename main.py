import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'проект', 'память']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')

posts = soup.find_all('article')
for post in posts:
    titles = post.find('a', class_='tm-article-snippet__title-link').text
    text = post.find('div', class_='article-formatted-body').text
    date = post.find('span', class_='tm-article-snippet__datetime-published').text
    href = post.find('a', class_='tm-article-snippet__title-link').get('href')
    for word in KEYWORDS:
        if word in text or word in titles:
            print(f'Дата: {date}, Заголовок: {titles}, Ссылка: {url + href}')




# if __name__ == '__main__':






