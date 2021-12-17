# Реализуйте метод update_developer, который изменяет значение поля в определенной строке.
# Метод update_developer получает параметры  developer_id (номер разработчика), field_idx (номер поля), value
# (значение, которе нужно обновить)
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
            key = int(developer_id)
            self.developers.pop(key)
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")

    def update_developer(self, developer_id, field_idx, value):
        developer = self.developers[developer_id]
        developer.update(field_idx, value)