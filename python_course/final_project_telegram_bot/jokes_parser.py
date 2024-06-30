import random
import requests
from bs4 import BeautifulSoup as BS
from topics_file import topics

class JokesParser():

    _main_url = 'https://www.anekdot.ru/tags/'

    # функция формирования ссылку
    def get_url(self):
        return self._main_url + input('Введите тему анекдота: ')


    # функция получения анекдотов по данной ссылке
    def parse_jokes(self, website_url):
        request = requests.get(website_url)
        soup = BS(request.text, 'html.parser')
        jokes = soup.find_all('div', class_='text')
        return [i.text for i in jokes if 0 < len(i.text) < 4096]


    # функция получения случайного анекдота дня
    def get_joke_day(self):
        joke_day_url = 'https://www.anekdot.ru/release/anekdot/day/'
        day_jokes = self.parse_jokes(joke_day_url)
        return day_jokes[random.randint(0, len(day_jokes) - 1)]


    # получение случайного анекдота из случайной темы
    def get_random(self):
        random_joke = self.parse_jokes(self._main_url + topics[random.randint(0, len(topics) - 1)])
        return random_joke[random.randint(0, len(random_joke) - 1)]

    # получение случайной шутки по теме
    def get_topic_joke(self, joke_topic):
        topic_joke_url = self._main_url + joke_topic
        topic_joke = self.parse_jokes(topic_joke_url)
        return topic_joke[random.randint(0, len(topic_joke) - 1)]