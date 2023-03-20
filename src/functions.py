from flask import Flask, request
import pandas as pd
from itertools import chain
import random


#  Получаем ссылку и параметры запроса
def get_categories():
    category = request.args.to_dict().values()
    print(f' Категории получены: {category}')
    if 0 < len(category) < 11:
        return category
    elif len(category) < 0:
        print("Ошибка: недопустимое значение категорий")
        return False
    else:
        return False


#  Получаем список из ссылок которые подходят под параметры запроса
def get_list_of_links(category_list):
    df = pd.read_csv('configuration.csv', sep=';')

    array_res = []
    categories = df.columns[2:]
    for i in category_list:
        for j in categories:
            tmp_res = list(df.loc[df[j] == i].url)
            if tmp_res:
                array_res.append(tmp_res)
    return list(chain(*array_res))


#  Ф-ия уменьшения кол-ва показов
def remove_one_show(link):
    df = pd.read_csv('configuration.csv', sep=';')

    for index, row in df.iterrows():
        if link in row['url']:
            # Уменьшить значение колонки на 1
            df.at[index, 'amount_of_shows'] -= 1
            df.to_csv('configuration.csv', index=False, sep=';')
