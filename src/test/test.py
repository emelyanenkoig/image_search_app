from flask import request

from src.functions import remove_one_show, get_list_of_links
import random

# Буфер недавних ссылок
recent_images = ['templates/images/bmw.png']


def get_data_test():
    # Очищаем буфер если надо
    if len(recent_images) > 3:
        recent_images.clear()

    # Получаем ссылку и параметры запроса
    category_list = request.args.to_dict().values()

    if category_list:
        # Считываем данные из конфигурационного файла
        list_of_links = get_list_of_links(category_list)
        print(f'Недавние ссылки {recent_images}')
        print(f'Список ссылок {list_of_links}')
        link1 = random.choice(list_of_links)
        print(f'Текущая ссылка {link1}')
        if link1 not in recent_images:
            print(link1)
            remove_one_show(link1)
            recent_images.append(link1)
            return link1
        else:
            print('Ссылка была в недавних ссылках:')
            list_of_links.remove(link1)
            print(f'Измененный список ссылок {list_of_links}')
            link1 = random.choice(list_of_links)
            print(f'Текущая ссылка {link1}')
            recent_images.append(link1)
            return link1

    else:
        print("Слишком много категорий ")
        return "Слишком много категорий "


# Разбиваю сслыку на части. Ищу имя файла
def split_url_test(link1):
    # Разбиваем url на части
    url_parts = link1.split('/')
    data = url_parts[4:]
    link1 = ''.join(data)
    url_parts = link1.split(';')
    url_parts = url_parts[0]

    # Возвращаем список данных
    return url_parts


link = 'http://localhost:8080/static/image2.jpg;500;flight;airlplane'
print(split_url_test(link))
# get_data_test()
