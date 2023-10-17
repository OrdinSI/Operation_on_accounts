import json


def get_operations():
    """ Получает данные из файла operations.json"""
    with open("operations.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data


def sort_key(e):
    """ Ключ для сортировки файла по дате"""
    return e["date"]


def remove_empty_items():
    """ Удаление пустых элементов из списка"""
    data = get_operations()
    return [d for d in data if "date" in d]


def sort_data():
    """ Сортировка данных по дате от большей к меньшей"""
    data = remove_empty_items()
    data.sort(reverse=True, key=sort_key)
    return data





