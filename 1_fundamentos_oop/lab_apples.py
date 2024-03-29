import random


class Apple:

    def __init__(self):
        self.weight = round(random.uniform(0.2, 0.5), 3)


class PackagingApple:
    WEIGHT_LIMIT = 300.000
    counter_apples = 0
    weight = 0

    def __init__(self, apples):
        self.add_apple(apples)

    def add_apple(self, apples):
        for _ in range(apples):
            apple = Apple()
            if round(PackagingApple.weight + apple.weight, 1) <= PackagingApple.WEIGHT_LIMIT:
                PackagingApple.counter_apples += 1
                PackagingApple.weight += apple.weight
            else:
                break


print("Processando o pedido")
pack_apple = PackagingApple(1000)
print("Pedido processado")
print("Total de maças:", pack_apple.counter_apples)
print("Peso total", round(pack_apple.weight, 3))
