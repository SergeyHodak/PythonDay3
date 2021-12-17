# Для класса AddressBook реализуйте метод add для добавления новых элементов:
#
# 1. метод add получает параметр developer;
# 2. в поле self.developers добавляем "новую строку" со значением параметра developer, номер которой
# соответствует значению self.last_developer_id;
# 3. после добавление нового элемента в словарь self.developers значение self.last_developer_id увеличиваем на 1.

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer
        self.last_developer_id += 1