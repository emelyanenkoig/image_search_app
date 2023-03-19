from flask import Flask, render_template, url_for, request
import pandas as pd
from itertools import chain
import random

app = Flask(__name__)


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


# Буфер недавних ссылок
recent_images = []


@app.route("/static")
def get_data():
    # Получаем ссылку и параметры запроса
    category_list = get_categories()

    # Очищаем буфер если надо
    if len(recent_images) > 3:
        recent_images.clear()

    if category_list:
        # Считываем данные из конфигурационного файла
        list_of_links = get_list_of_links(category_list)
        random_link = random.choice(list_of_links)
        if random_link not in recent_images:
            print(random_link)
            remove_one_show(random_link)
            return random_link

    else:
        print("Слишком много категорий ")
        return "Слишком много категорий "


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
