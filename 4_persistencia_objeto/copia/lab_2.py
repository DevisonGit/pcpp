import copy


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return str(self.__dict__)

    def discount(self):
        if self.weight > 300:
            self.price -= self.price * 20 / 100
        return self


warehouse_list_object = list()
warehouse_list = [{'name': 'Lolly Pop', 'price': 0.4, 'weight': 133},
                  {'name': 'Licorice', 'price': 0.1, 'weight': 251},
                  {'name': 'Chocolate', 'price': 1, 'weight': 601},
                  {'name': 'Sours', 'price': 0.01, 'weight': 513},
                  {'name': 'Hard candies', 'price': 0.3, 'weight': 433}]

for candy in warehouse_list:
    warehouse_list_object.append(Delicacy(**candy))

print("*" * 20, "Original")
for candy in warehouse_list_object:
    print(candy)

# deepcopy
print("*" * 20, "Deepcopy")
warehouse_list_copy = copy.deepcopy(warehouse_list_object)
warehouse_list_copy = [candy.discount() for candy in warehouse_list_copy]
for candy in warehouse_list_copy:
    print(candy)

