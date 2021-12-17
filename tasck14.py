# Формат JSON можно преобразовать только в простые структуры. А наша система работает
# на классах (более сложной структуры, которую нельзя напрямую получить из JSON).
# Поэтому нам необходимо из полученного из JSON-строки словаря создать объект с нужными данными.

# 1. Переменной elem присвойте объект, в котором хранится информация о разработчиках из
# JSON-строки jsn.
# 2. Переменной obj присвойте объект класса FirstNameField, со значением поля value равное значению,
# которое хранится в объекте elem по ключу value.

import json


class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"


class FirstNameField(DataField):
    field_description = "Name"


jsn ='{"value": "Ivan", "field_name": "Name"}'
elem = json.loads(jsn)

key = elem["value"]
obj = FirstNameField(key)
print(obj)