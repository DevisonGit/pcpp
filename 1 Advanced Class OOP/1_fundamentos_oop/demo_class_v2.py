class Demo:
    class_var = "shared variable"


d1 = Demo()
d2 = Demo()

# ambas as instancias permitem acesso a variavel de class
print(d1.class_var)
print(d2.class_var)
print("*" * 20)

# objeto d1 não possui variavel de instancia
print("contents of d1", d1.__dict__)
print("*" * 20)

# objeto d1 recebe uma variavel de instancia chamada class_var
d1.class_var = "I'm messing with class variable"

# o objeto d1 possui a variavel chamada class_var que contem um valor diferente da variavel de classe com mesmo nome
print("contents of d1", d1.__dict__)
print(d1.class_var)
print("*" * 20)

# variaveis do objeto d2 não foram influenciadas
print("contents of d2", d2.__dict__)

print("contents of class variable accessed via d2", d2.class_var)
