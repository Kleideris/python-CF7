bag = {"eggs", "oranges", "bananas", "eggs"}
print("Initial bag:", bag)

# add a new item
bag.add("grapes")
print("bag after adding grapes", bag)

# remove
bag.remove("bananas")
print("bag after removing bananas", bag)

#bag.remove("melon")  # will throw KeyError

for item in bag:
    print(item, end=" ")
print()