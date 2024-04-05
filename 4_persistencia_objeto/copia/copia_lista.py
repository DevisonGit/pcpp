print("Part 1")
print("Let's make a copy")
list_a = [10, 'banana', [997, 123]]
list_b = list_a[:]
print("list_a", list_a)
print("list_b", list_b)
print("Is it the same object?", list_a is list_b)
print("Part 2")
print("Let's modify list_b[2]")
list_b[2][0] = 112
print("list_a", list_a)
print("list_b", list_b)
print("Is it the same object?", list_a is list_b)
