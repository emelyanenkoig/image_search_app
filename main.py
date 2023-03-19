import csv, pprint
import flask
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Буфер недавних ссылок
recent_images = []


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


# Считываем данные из конфигурационного файла
def read_config_file():
    csvfile = open("configuration.csv", newline='')
    reader = csv.DictReader(csvfile, delimiter=';')
    return reader


#  Ищем совпадающие категории
def find_a_match(reader, category_list):
    for row in reader:
        for column in row:
            print(recent_images)
            if row[column] in category_list:
                if row['url'] not in recent_images:
                    # Добавить в буфер ссылку
                    recent_images.append(row['url'])

                    # Изменить количество показов
                    return row['url']
                else:
                    continue
    return "Совпадающих категорий не было найдено"


def rewrite_csvfile():
    csvfile = open("configuration.csv", newline='')
    fieldnames = ['amount_of_shows']
    reader = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    return reader


@app.route("/static")
def get_data():
    # Получаем ссылку и параметры запроса
    category_list = get_categories()

    # Очищаем буфер если надо
    if len(recent_images) > 3:
        recent_images.clear()

    if category_list:
        # Считываем данные из конфигурационного файла
        csvfile = read_config_file()
        match = find_a_match(csvfile, category_list)
        print(f' Недавние изображения: {recent_images}')

        return match
    else:
        print("Слишком много категорий ")
        return "Слишком много категорий "


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

# # Создаем искусственно контекст запроса
# with app.test_request_context():
#     print(url_for('get_data'))
#     print(url_for('about'))

# "/static/<path:image>;<int:amount_of_shows>;<path:category>;<path:category>"
