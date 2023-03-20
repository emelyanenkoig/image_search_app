from src.functions import get_categories, get_list_of_links, remove_one_show
from flask import Flask, render_template
import random

app = Flask(__name__)

# Буфер недавних ссылок
recent_images = []


@app.route("/static")
def get_data():

    # Очищаем буфер если надо
    if len(recent_images) > 3:
        recent_images.clear()

    # Получаем ссылку и параметры запроса
    category_list = get_categories()

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
