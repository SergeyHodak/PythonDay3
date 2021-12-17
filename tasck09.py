# Реализуйте список lst таким образом, чтобы его JSON-дамп jsn имел вид [5,6,7,8].

import json
lst = []

lst.append(5)
lst.append(6)
lst.append(7)
lst.append(8)

jsn = json.dumps(lst)
print(jsn)