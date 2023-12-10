import json

def read_obj(obj, numbers):
    if type(obj) is dict:
        if 'red' not in obj.values():
            for i, o in enumerate(obj.values()):
                numbers.append(read_obj(o, numbers))
    elif type(obj) is list:
        for i, o in enumerate(obj):
            numbers.append(read_obj(o, numbers))
    else:
        if type(obj) is int:
            return obj
        else:
            return 0
    return 0

with open('./day12.json', 'r') as f:
    data = json.load(f)
    idx = 0
    numbers = []
    read_obj(data, numbers)
    print(sum(numbers))