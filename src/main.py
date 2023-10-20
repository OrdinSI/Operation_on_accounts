from datetime import datetime as dt

from src.utils import *


def data_masking(data, request_type: str):
    parts = data.split()
    last_part = parts[-1]
    if request_type == 'from':
        masked_last_part = last_part[:4] + ' ' + last_part[4:6] + '**' + ' ' + '****' + ' ' + last_part[-4:]
    else:
        masked_last_part = last_part[:4] + ' ' + '****' + ' ' + '****' + ' ' + last_part[-4:]
    masked_s = ' '.join(parts[:-1] + [masked_last_part])
    return masked_s


def main():
    datas = get_result_data()
    results = []
    for data in datas:
        data_masked_to = data_masking(data['to'], "to")
        date_obj = dt.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_obj.strftime("%d.%m.%Y")
        if 'from' in data:
            data_masked_from = data_masking(data['from'], "from")
            result = (f"{formatted_date} {data['description']}\n"
                      f"{data_masked_from} -> {data_masked_to}\n"
                      f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")
        else:
            result = (f"{formatted_date} {data['description']}\n"
                      f"{data_masked_to}\n"
                      f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")
        results.append(result)
    return results


if __name__ == '__main__':
    for result in main():
        print(result)

