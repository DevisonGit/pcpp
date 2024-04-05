a_list = ["First error", "Second error"]

try:
    print(a_list[3])
except Exception as e:
    try:
        print(1/0)
    except ZeroDivisionError as f:
        print("Inner Exception (f)", f)
        print("Outer Exception (e)", e)
        print("Outer Exception referenced", f.__context__)
        print("Is it the same object:", f.__context__ is e)
