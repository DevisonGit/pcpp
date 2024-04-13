a = '10 days to departure'
b = a

print("a identity", id(a))
print("b identity", id(b))
print("The result of the value comparison", a == b)
print("The result of the identity comparison", a is b)

a = ['10', 'days to departure']
b = ['10', 'days to departure']

print("a identity", id(a))
print("b identity", id(b))
print("The result of the value comparison", a == b)
print("The result of the identity comparison", a is b)
