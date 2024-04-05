import copy


class Example:
    def __init__(self):
        self.property = ['112', '997']
        print("Hello from __.init__()")


print("Deep copy")
a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks", id(a_example), id(b_example))
print("Same memory?", a_example is b_example)
print("\nLet's modify the movies list")
b_example.property.append("911")
print("a_example.properties", a_example.property)
print("b_example.properties", b_example.property)
