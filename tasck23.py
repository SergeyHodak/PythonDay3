# Модифицируйте функцию search так, чтобы если передан не Query-параметр 'all', переменная
# search_result получала результаты поиска по некоторым полям (метод AB.multiple_search с
# параметром **search_query).

from flask import Flask, request, jsonify


class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer
        self.last_developer_id += 1

    def str_search(self, search_str: str):
        result = {}
        for developer_id, developer in self.developers.items():
            if search_str in developer:
                result[developer_id] = developer
        return result

    def multiple_search(self, **search_items):
        result = {}
        for developer_id, developer in self.developers.items():
            if developer.multiple_search(**search_items):
                result[developer_id] = developer
        return result


AB = AddressBook()
app = Flask("answer")


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(message=str(e))


@app.route("/ab/search")
def search():
    search_query = request.args.to_dict()
    search_result = {}
    if "all" in search_query:
        search_result = AB.str_search(search_query["all"])
    else:
        search_result = AB.multiple_search(**search_query)
    search_result_dict = {}

    for key, rec in search_result.items():
        search_result_dict[str(key)] = rec.to_dict()
    response = jsonify(**search_result_dict)
    return response