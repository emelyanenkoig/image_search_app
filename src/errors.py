def too_much_error_message():
    message = 'Слишком много'
    return message


def no_category_error_message():
    message = 'Нет категории'
    return message


class TooMuchElementsError(Exception):
    pass


class NoCategoryError(Exception):
    pass