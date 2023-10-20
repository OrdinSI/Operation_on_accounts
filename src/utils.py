import json


def get_operations():
    """ Получает данные из файла operations.json"""
    with open("operations.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data


def remove_empty_items():
    """ Удаление пустых элементов из списка"""
    data = get_operations()
    return [d for d in data if "date" in d]


def sort_key(e):
    """ Ключ для сортировки файла по дате"""
    return e["date"]


def sort_data():
    """ Сортировка данных по дате от большей к меньшей"""
    data = remove_empty_items()
    data.sort(reverse=True, key=sort_key)
    return data


def get_result_data():
    """Получение первых number_last значений для отображения"""
    number_last = 5
    result_data = []
    datas = sort_data()
    for data in datas:
        if data['state'] == "EXECUTED" and number_last > 0:
            number_last -= 1
            result_data.append(data)
    return result_data




