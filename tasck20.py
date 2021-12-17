# Модифицируйте функцию search так, чтобы переменная response получила словарь Query-параметров из запроса.

from flask import Flask, request


app = Flask("answer")


@app.route("/ab/search")
def search():
    response = request.args.to_dict()
    return response