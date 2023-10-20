from datetime import datetime as dt

from src.utils import *


def data_masking(data, request_type: str):
    """Функция для маскировки даты"""
    parts = data.split()
    last_part = parts[-1]
    if request_type == 'from':
        masked_last_part = last_part[:4] + ' ' + last_part[4:6] + '**' + ' ' + '****' + ' ' + last_part[-4:]
    else:
        masked_last_part = last_part[:4] + ' ' + '****' + ' ' + '****' + ' ' + last_part[-4:]
    return ' '.join(parts[:-1] + [masked_last_part])


def format_date(data):
    """Форматирование даты"""
    date_obj = dt.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


def format_result(data, formatted_date):
    """Форматирование результата"""
    data_masked_to = data_masking(data['to'], "to")
    if data.get('from'):
        data_masked_from = data_masking(data['from'], "from")
        result_data = (f"{formatted_date} {data['description']}\n"
                       f"{data_masked_from} -> {data_masked_to}\n"
                       f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")
    else:
        result_data = (f"{formatted_date} {data['description']}\n"
                       f"{data_masked_to}\n"
                       f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")

    return result_data


def main():
    """ Программа для вывода 5 последних операций по счету"""
    datas = get_result_data()
    results = []
    for data in datas:
        formatted_date = format_date(data)
        result_data = format_result(data, formatted_date)
        results.append(result_data)
    return results


if __name__ == '__main__':
    for result in main():
        print(result + '\n')
