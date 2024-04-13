import pickle


a_list = ['a', 123, [10, 100, 1000]]
bytes_inter = pickle.dumps(a_list)
print("Intermediate a object type, used to preserve data:", type(bytes_inter))

b_list = pickle.loads(bytes_inter)
print("A type of deserialized object", type(b_list))
print("contents", b_list)
