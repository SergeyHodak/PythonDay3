# На вход new_field приходит JSON-строка в теле запроса. В JSON сериализирован словарь
# с ключом 'name'. Измените функцию new_field так, чтобы в переменной field_name
# сохранялось значение из тела запроса по ключу 'name'.

from flask import Flask, request

app = Flask("answer")

@app.route("/ab/developer/<developer_id>/field", methods=["POST"])
def new_field(developer_id):
    field_name = request.json["name"]
    return f"Name {field_name}, developer: {developer_id}"