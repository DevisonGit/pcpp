import random


class Apple:
    lower = 0.2
    upper = 0.5
    counter = 0
    weight_limit = 300
    total_weight = 0

    def __init__(self, weight) -> None:
        self.weight = weight
        Apple.counter += 1
        Apple.total_weight += self.weight


for _ in range(1000):
    weight =  random.uniform(Apple.lower, Apple.upper)
    if Apple.total_weight + weight <= Apple.weight_limit:
        apple = Apple(weight=weight)
    else: 
        break

print("number of apples: {}".format(Apple.counter))
print("total weight: {}".format(Apple.total_weight))

