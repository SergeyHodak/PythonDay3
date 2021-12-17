# 1. Создайте класс AddressBook, в котором будет реализован метод __init__
# 2. В методе __init__ заданы 2 поля: self.developers со значением пустого словаря ({})
# и self.last_developer_id со значением 0
# 3. Создайте адресную книгу разработчиков (объект ab класса AddressBook)
class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0


ab = AddressBook()