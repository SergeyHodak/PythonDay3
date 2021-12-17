# У нас есть информация о разработчиках, сохраненная в формате JSON (как текстовый файл).
# Чтобы начать работать с этой информацией нам нужно ее передать нашей программе. То есть
# преобразовать JSON-строку в список словарей, чтобы наша система могла работать с этими
# данными о зарплатах разработчиков.
# Это важно сделать, потому что система напрямую с JSON работать не может, а со списком
# словарей - может. Поэтому в этой задаче учимся читать из формата JSON список словарей.

# 1. Получите объект, в котором хранится информация о разработчиках из JSON-строки jsn.
# 2. Присвойте переменной name_3 имя третьего по счету разработчика.
# 3. Присвойте переменной rate_1_2_3 сумму уровней оплат разработчиков.

import json

jsn ='''{
"0": {"fields": [
    {"value": "Vlad", "field_name": "Name"}, 
    {"value": 1300, "field_name": "Rate"}]}, 
"1": {"fields": [
    {"value": "Max", "field_name": "Name"}, 
    {"value": 1200, "field_name": "Rate"}]}, 
"2": {"fields": [
    {"value": "Ivan", "field_name": "Name"}, 
    {"value": 2800, "field_name": "Rate"}]}
}'''

elem = json.loads(jsn)

name_3 = elem["2"]['fields'][0]['value']

rate_1_2_3 = elem['0']['fields'][1]['value'] + elem["1"]['fields'][1]['value'] + elem["2"]['fields'][1]['value']