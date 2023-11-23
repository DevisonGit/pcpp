class MobilePhone:
    def __init__(self, number):
        self.number = number


    def turn_on(self):
        return f'mobile phone {self.number} is turned on'
    

    def turn_off(self):
        return 'mobile phone is turned off'
    
    def call(self, number):
        return f"calling {number}"


phone_one = MobilePhone("01632-960004")
phone_two = MobilePhone("01632-960012")

print(phone_one.turn_on())
print(phone_two.turn_on())

print(phone_one.call("555-34343"))

print(phone_one.turn_off())
print(phone_two.turn_off())