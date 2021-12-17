# Добработайте метод delete с параметром developer_id так, чтобы он:
#
# 1. удалял из словаря self.developers запись по ключу, который соответствует значению параметра developer_id.
# 2. использовал конструкцию try ... except при приведении значения параметра к целому числу (int),
# а также при удалении элемента из словаря.
# 3. при возникновении исключения TypeError (параметр, который передан не может быть приведен к целому числу)
# вызывается исключение с f-строкой: f"Developer ID {developer_id} is not int"
# 4. при возникновении исключения KeyError (в словаре self.developers отсутствует запись с таким ключом)
# вызывается исключение с f-строкой: f"Developer {developer_id} not found"
# 5. удалял из словаря self.developers запись по ключу key, а также вызывал собственное исключение IncorrectInput.

class IncorrectInput(Exception):
    pass

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        try:
            self.developers.pop(int(developer_id))
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")