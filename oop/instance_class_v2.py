class Demo:
    class_var = "shared variable"

d1 = Demo()
d2 = Demo()

# both instance allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance varible
print("contents of d1 ", d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"

print("contents of d1 ", d1.__dict__)
print(d1.class_var)
print('.' * 20)

print("contents of d2 ", d2.__dict__)
print("contents of class variable accessed via d2 ", d2.class_var)