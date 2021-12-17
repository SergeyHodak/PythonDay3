# Добавьте словарю developer:
# 1. По ключу Name значение Peter
# 2. По ключу Rate значение 1800

from flask import Flask, jsonify

developer = {"Name": "Peter", "Rate": "1800"}

app = Flask("developer")


@app.route("/developer")
def developer_out():
    response = jsonify(developer)
    return response