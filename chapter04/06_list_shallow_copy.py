my_list = [1, 2, "Hello", [3, 4, 5]]

# shallow copy using slicing
new_list = my_list[:]

print(f"Are new_list and my_list the same pbject: {my_list is new_list}")

print(id(my_list))
print(id(new_list))

my_list[0] = 100

print(f"Original list: {my_list}")
print(f"Shallow copy list: {new_list}")

my_list[3][0] = 300
print(f"Original list: {my_list}")
print(f"Shallow copy list: {new_list}")
print(my_list, id(new_list[0]), sep=", ")
print(new_list, id(new_list[0]), sep=", ")