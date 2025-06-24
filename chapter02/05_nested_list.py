items = [1, 2, 3.14, True, "Hello CF7 friends"]

for item in items:
    print(item, end=" ")
print()

nest_list = [
    [1,2],
    [3,4],
    [5,6],
    True,
]

# nest_list = [[1,2], [3,4], [5,6], True]

print(nest_list)

print(f"first list item: {nest_list[0]}")

# i want to get the '3'
print(f"{nest_list[1][0]}")  # 3

# [3,4], [1,2]
print(nest_list[1], nest_list[0], sep=", ")

#with slicing
print(nest_list[-3::-1])