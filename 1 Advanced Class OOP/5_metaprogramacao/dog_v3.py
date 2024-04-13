Dog = type("Dog", (), {})

print("the class name is", Dog.__name__)
print("The class is an instance of", Dog.__class__)
print("The class is based on", Dog.__bases__)
print("The class attributes", Dog.__dict__)
