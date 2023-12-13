class Car:
    def __init__(self, vin) -> None:
        print("ordinary __init__ was called for", vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print("class method was called")
        _car = cls(vin)
        _car.brand = brand
        return _car
    
car1 = Car("ABCD1234")
card2 = Car.including_brand("DEF567", "NewBrand")

print(car1.vin, car1.brand)
print(card2.vin, card2.brand)
