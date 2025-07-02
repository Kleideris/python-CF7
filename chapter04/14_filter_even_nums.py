"""
# can we create the list in an alternative way?

num = list(range(1,11))
numbers = [n for n in range(1, 11)]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(type(even_numbers))
'''
for num in even_numbers:
    print(num, end=" ")
print()
print("------------------")

for num in even_numbers:
    print(num, end=" ")
print()
'''

print(even_numbers)  # this will return the ""memory id""" of the filtered object i created.
print(*even_numbers)
print("---------------------")
print(*even_numbers)

# list
even_num_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_num_list)
print(even_num_list)
print("----------------")
print()

def even_num_func(n):
    return n % 2 == 0

my_list = list(filter(even_num_func, numbers))
print(my_list)