import datetime
import math
import json

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime('%A'))  # День недели

# x = datetime.datetime(2020, 5, 17)
# print(x)
#
#
# x = min(5, 10, 25)
# y = max(5, 10, 25)
#
# print(x, y)
#
# x = abs(- 7.25)
# print(x)
# x = pow(4,3)
#
# print(x)
#
# x = math.sqrt(64)
# x = math.ceil(1.4)
# x = math.floor(1.4)

# some JSON:
x = '{"name":"Alex", "age":20, "city":"Falesti"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
    "name":"Mihai",
    "age":21,
    "city":"Chisinau"
}

print(json.dumps({'name': 'John', 'age':30}))
print(json.dumps(['apple', 'bananas']))
print(json.dumps(('apple', 'bananas')))
print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# a Python object (dict)
x = {
    'name': 'Mihai',
    'age': 21,
    'city': 'Chisinau'
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'children': ('Ann', 'Billy'),
    'pets': None,
    'cars': [
        {'model': 'BMW 230', 'mpg': 27.5},
        {'model': 'Ford Edge', 'mpg':24.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
