from flask import request, render_template
import pandas as pd
from itertools import chain
import random
from src.errors import TooMuchElementsError, NoCategoryError
from loguru import logger
from config import recent_images


#  Получаем ссылку и параметры запроса
def get_categories():
    category = request.args.to_dict().values()
    logger.info(f' Категории получены: {category}')
    # Проверяем валидность входных данных
    if len(category) > 10:
        raise TooMuchElementsError
    return category


#  Получаем список из ссылок которые подходят под параметры запроса
def get_list_of_links(category_list):
    df = pd.read_csv('src/configuration.csv', sep=';')

    array_res = []
    categories = df.columns[2:]
    for i in category_list:
        for j in categories:
            tmp_res = list(df.loc[df[j] == i].url)
            if tmp_res:
                array_res.append(tmp_res)
    # Проверяем валидность возвращаемого списка
    if not array_res:
        raise NoCategoryError
    return list(chain(*array_res))


#  Ф-ия уменьшения кол-ва показов
def remove_one_show(link):
    df = pd.read_csv('src/configuration.csv', sep=';')

    for index, row in df.iterrows():
        if link in row['url']:
            # Уменьшить значение колонки на 1
            df.at[index, 'amount_of_shows'] -= 1
            df.to_csv('src/configuration.csv', index=False, sep=';')


def split_url(link):
    # Разбиваем url на части
    url_parts = link.split('/')
    data = url_parts[4:]
    link = ''.join(data)
    url_parts = link.split(';')
    url_parts = url_parts[0]

    # Возвращаем список данных
    return url_parts


def get_data():

    # Очищаем буфер если надо
    if len(recent_images) > 3:
        recent_images.clear()

    try:

        # Получаем параметры запроса
        category_list = get_categories()
        try:

            # Получаем список url изображений
            # которые подходят под параметры запроса
            list_of_links = get_list_of_links(category_list)

            # Выбираем случайную из списка
            link = random.choice(list_of_links)
            logger.info(f'Недавние изображения: {recent_images}')

            # Проверяем есть ли текущая ссылка в буфере
            if link not in recent_images:
                logger.info(f'Текущая ссылка {link}')
                remove_one_show(link)
                recent_images.append(link)
                link = split_url(link)

                return render_template('image.html', link=link)

            else:
                if len(list_of_links) > 1:
                    #  Базовый случай
                    list_of_links.remove(link)
                    link = random.choice(list_of_links)
                else:
                    # Проверка если повторяется запрос
                    # с одним и тем же параметром
                    link = random.choice(list_of_links)
                recent_images.append(link)
                logger.info(link)
                link = split_url(link)
                logger.info(f'Текущая ссылка {link}')

                return render_template('image.html', link=link)

        except NoCategoryError:
            logger.error('Нет подходящей категории для '
                         'данных параметров запроса')
            return 'Нет подходящей категории для ' \
                   'данных параметров запроса'

    except TooMuchElementsError:
        logger.error('Слишком много элементов в запросе')
        return 'Слишком много элементов в запросе'
