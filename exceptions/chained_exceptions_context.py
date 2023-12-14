a_list = ["First Error", "Second Error"]

try:
    print(a_list[3])
except Exception as e:
    try:
        print(1/0)
    except ZeroDivisionError as f:
        print("Inner exception (f):", f)
        print("Outer exception (e):", e)
        print("Outer exception referenced:", f.__context__)
        print("Is it the same object:", f.__context__ is e)
