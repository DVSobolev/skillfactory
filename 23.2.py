# Добрый день! Уже неделю не могу решить домашнее задание, поэтому прошу помощи:
#
# 1 вариант кода. Данный вариант выводит наименоdание фильма, год выпуска фильма и оценку фильма, результат выполнения кода:
# [{'Наименование фильма': 'Враг государства', 'Год выпуска фильма/сериала': '1998', 'Оценка фильма': '7'}, {'Наименование фильма': 'Перл-Харбор', 'Год выпуска фильма/сериала': '2001', 'Оценка фильма': '8'}, {'Наименование фильма': 'Миллионер из трущоб', 'Год выпуска фильма/сериала': '2008', 'Оценка фильма': '9'}, {'Наименование фильма': 'Шерлок Холмс: Игра теней', 'Год выпуска фильма/сериала': '2011', 'Оценка фильма': '9'}, {'Наименование фильма': 'Однажды в Америке', 'Год выпуска фильма/сериала': '1983', 'Оценка фильма': '8'}]
# но он периодически (со временем) падает в ошибку, не понимаю с чем это связано

# import requests
# from bs4 import BeautifulSoup
#
# user_login = '1668582'
# page_num = 13
# url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}'
# html_content = requests.get(url)
# soup = BeautifulSoup(html_content.text, 'lxml')
# entries = soup.find('div', class_='profileFilmsList')
# itm = entries.find_all('div', class_='item')
#
# data = []
# for entry in itm:
#     film = entry.find('div', class_='nameRus').find('a')
#     film_name = film.text.split(' (')[0]
#     film_year = film.text.split(' (')[1].rstrip(')').lstrip('сериал, ').lstrip('мини-сериал, ')
#     film_vote = entry.find('div', class_='vote')
#     data.append({'Наименование фильма': film_name, 'Год выпуска фильма/сериала': film_year, 'Оценка фильма': film_vote.text})
#
# print(data[:5])

# 2 вариант кода. Данный вариант написан по рассматриваемому примеру в курсе, но код не выводит результат, если в переменную entries добавить find('div', class_='profileFilmsList'). в начало, то возникнет ошибка:
# entries = soup.find('div', class_='profileFilmsList').find_all('div', class_='item')
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_user_rates(user_login):
    page_num = 1
    data = []

    while True:
        url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/{page_num}'
        html_content = requests.get(url)
        soup = BeautifulSoup(html_content.text, 'lxml')
        entries = soup.find_all('div', class_='item')

        if len(entries) == 0:  # Признак остановки
            break

        for entry in entries:
            film = entry.find('div', class_='nameRus').find('a')
            film_name = film.text.split(' (')[0]
            film_year = film.text.split(' (')[1].rstrip(')').lstrip('сериал, ').lstrip('мини-сериал, ')
            film_vote = entry.find('div', class_='vote')
            data.append({'Наименование фильма': film_name, 'Год выпуска фильма/сериала': film_year, 'Оценка фильма': film_vote.text})

        page_num += 1

    return data

user_rates = collect_user_rates(user_login = '1668582')
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')