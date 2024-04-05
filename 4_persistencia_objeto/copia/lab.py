import copy


warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print("Source list of candies")
for candy in warehouse:
    print(candy)

print("*" * 20)
print("Price Proposal")
warehouse_copy = copy.deepcopy(warehouse)
for candy in warehouse_copy:
    if candy['weight'] > 300:
        candy['price'] -= (candy['price'] * 20) / 100

for candy in warehouse_copy:
    print(candy)
