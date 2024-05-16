import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + " is not JSON serializable")


def decode_who(w):
    return Who(w['name'], w['age'])


some_man = Who("John Doe", 42)
json_man = json.dumps(some_man, default=encode_who)
new_man = json.loads(json_man, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)
