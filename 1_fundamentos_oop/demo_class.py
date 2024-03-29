class Demo:
    class_var = "shared variable"


print(Demo.class_var)
print(Demo.__dict__)

d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)
print("contents of d1", d1.__dict__)
