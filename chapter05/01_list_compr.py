list_of_ints = [1, 2, 3, 4, 5, 6, 7]

# 1. squared nums using list compr
sq_nums_compr = [num ** 2 for num in list_of_ints]
print(sq_nums_compr)

# 2. squared nums using map functions
sq_nums_map = list(map(lambda num: num ** 2, list_of_ints))
print(sq_nums_map)

# 3. squared nums using a function
def squared_function(num):
    return num ** 2

sq_nums_func = [squared_function(num) for num in list_of_ints if num < 5]
print(sq_nums_func)

# 4. 'square function and map'
sq_map_func = list(map(sq_map_func, list_of_ints))
print(sq_map_func)

# 5 filter and square only with list comp
fitlered_sq_list_compr = [num ** 2 for num in list_of_ints if num < 5]
print(fitlered_sq_list_compr)
