# Используйте словарь, в котором задана информация о разработчике
# 1. Создайте переменную developer2, которой присвойте описание разработчика: имя (name) Vlad,
# уровень оплаты (Rate) 2300.
# 2. Создайте переменную developer3, которой присвойте описание разработчика: имя (name) Ivan,
# уровень оплаты (Rate) 2700.
# 3. Создайте список developer_list, который состоит из переменных developer1, developer2, developer3.
# 4. Получите значение переменной jsn, как результат сериализации переменной developer_list.

import json

developer1 = {'name': 'Max', 'rate': 1500}
developer2 = {'name': 'Vlad', 'rate': 2300}
developer3 = {'name': 'Ivan', 'rate': 2700}
developer_list = [developer1, developer2, developer3]
jsn = json.dumps(developer_list)