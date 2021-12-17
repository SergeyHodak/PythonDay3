# Напишите метод delete так, чтобы он удалял из словаря self.developers запись по ключу key:
#
# 1. метод получает параметр developer_id
# 2. переменная key получает значение developer_id приведенное к типу int
# 3. с помощью метода pop из словаря self.developers удаляется элемент с номером key

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        key = int(developer_id)
        self.developers.pop(key)