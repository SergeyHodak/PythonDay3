# 1. Задание значение JSON-строки jsn (["name","city","skill","rate","phone"]).
# 2. Получите значение переменной obj как результат десериализации JSON-строки jsn

import json

jsn = '["name","city","skill","rate","phone"]'
obj = json.loads(jsn)
print(obj)