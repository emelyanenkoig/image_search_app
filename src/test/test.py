from src.functions import *

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
        link = random.choice(list_of_links)
        print(f'Текущая ссылка {link}')
        if link not in recent_images:
            print(link)
            remove_one_show(link)
            recent_images.append(link)
            return link
        else:
            print('Ссылка была в недавних ссылках:')
            list_of_links.remove(link)
            print(f'Измененный список ссылок {list_of_links}')
            link = random.choice(list_of_links)
            print(f'Текущая ссылка {link}')
            recent_images.append(link)
            return link

    else:
        print("Слишком много категорий ")
        return "Слишком много категорий "


get_data_test()