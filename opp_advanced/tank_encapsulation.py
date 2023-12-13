class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, amount):
        if amount > 0:
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError("too much liquid in the tank")
        elif amount < 0:
            raise TankError("Not possible to set negative liquid level")
        
    @level.deleter
    def level(self):
        if self.__level > 0:
            print("It is good to remember to sanitize the remains from the tank")
        self.__level = None

our_tank = Tank(20)

our_tank.level = 10
print("current liquid level:", our_tank.level)

our_tank.level += 3
print("current liquid level:", our_tank.level)

try:
    our_tank.level = 21
except TankError as e:
    print("Trying to set liquid level to 21 inits, result", e)

try:
    our_tank.level += 15
except TankError as e:
    print("Trying to add an additioinal 15 units, result", e)

try:
    our_tank.level = -3
except TankError as e:
    print("Trying to set liquid level to -3, result", e)

print("current liquid level:", our_tank.level)

del our_tank.level