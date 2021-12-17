# Используйте словарь, в котором задана информация о разработчике
# 1. Измените уровень оплаты разработчика на 2000.
# 2. Получите значение переменной jsn как результат сериализации объекта developer

import json

developer = {
    'Name': 'Serhii',
    'City': 'Kyiv',
    'Skill': 'Python',
    'Phone': '+380631234567',
    'Rate': 1700
}
developer['Rate'] = 2000
jsn = json.dumps(developer)