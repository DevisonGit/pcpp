class Demo:
    def __init__(self, value):
        # variable of instance
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)

# instance variable created during any moment
d1.another_var = "another variable in the object"

print("contents of d1's", d1.__dict__)
print("contents of d2's", d2.__dict__)
