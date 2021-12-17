# Супер, вы уже делаете практически невозможное для джуна.
# Осталось поставить преобразование словарей в объекты на поток. Для этого напишите
# специальную функцию, которая будет получать словарь с названием класса и его
# начальным значением и возвращать новый объект.

# Доработайте функцию field_decoder, которая:

# 1. получает словарь, созданный из JSON-строки (json_in).
# 2. переменной name присваивает значение словаря по ключу field_name, переменной value
# присваивает значение словаря по ключу value (строки 41 и 42)
# 3. переменная base_class получает объект, соответствующий значению перменной name
# (при значении "Name" - FirstNameField, при значении "Rate" - RateField) (строка 44)
# 4. возвращаемый объект должен получить значение, которое соответствует значению
# словаря по ключу value (строка 45)

class DataField:
    field_description = "General"
    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}: {self.value}"

class FirstNameField(DataField):
    field_description = "Name"

class RateField(DataField):
    field_description = "Rate"


REGISTERED_FIELDS = {
    FirstNameField.field_description: FirstNameField,
    RateField.field_description: RateField
    }

def field_decoder(json_in):
    name = json_in["field_name"]
    value = json_in["value"]

    base_class = REGISTERED_FIELDS[name]
    field = base_class(value)
    return field