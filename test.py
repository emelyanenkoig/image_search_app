import csv
from pprint import pprint
import pandas
import flask
from flask import Flask, render_template, url_for, request
import pandas as pd
from itertools import chain
import random

# # create DataFrame
# df_test = pd.DataFrame({'url': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'amount': [5, 7, 7, 9, 12, 9, 9, 4],
#                         'cat1': [11, 8, 10, 6, 6, 5, 9, 12],
#                         'cat2': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat3': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat4': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat5': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat6': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat7': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat8': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat9': [25, 12, 15, 14, 19, 23, 25, 29],
#                         'cat10': [25, 12, 15, 14, 19, 23, 25, 29]
#                         })
# df_test.at[1, 'amount'] = 100000
# df_test.to_csv('test.csv', index=False, sep=';')

category = ['vechile', 'animals']


#  Получаем список ссылок
def get_list_of_links(category_list):
    df = pd.read_csv('configuration.csv', sep=';')
    categories = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9', 'cat10']
    array_res = []

    for i in category_list:
        for j in categories:
            tmp_res = list(df.loc[df[j] == i].url)
            if tmp_res:
                array_res.append(tmp_res)
    return list(chain(*array_res))


def remove_one_show(link):
    df = pd.read_csv('configuration.csv', sep=';')
    amount = df.loc[df.url == link, ['amount_of_shows']]
    # df.loc[df.url == link]['amount_of_shows'] = df.loc[df.url == link]['amount_of_shows'] - 1
    # print(df.loc[df.url == link]['amount_of_shows'])
    # df.to_csv('configuration.csv', index=False, sep=';')


list_of_links = get_list_of_links(category)
random_link = random.choice(list_of_links)
print(random_link)
remove_one_show(random_link)

# df['merge_column'] = df[['cat1', 'cat2', 'cat3', 'cat4', 'cat5',
#                          'cat6', 'cat7', 'cat8', 'cat9', 'cat10']].values.tolist()
