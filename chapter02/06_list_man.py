fruits = ["Apple", "Banana", "Cherry", "Apple"]

print(f"Initial list: {fruits}")

# Add a fruit at the end of the list
fruits.append("Berry")

print("After adding Berry:", fruits)

# fruits.append(["Grapes", "Figs"])
# print("after adding Grapes, Figs with append:", fruits)

fruits.extend(["Grapes", "Figs"])
print("after adding Grapes, Figs with extend:", fruits)

# insert an element in specific position
fruits.insert(1, "Coconut")
print("after adding Coconut:", fruits)

# Update the first element
fruits[0] = "Melon"
print("after updating the first element:", fruits)

# Update a slice of list (two elements)
fruits[1:3] = ["A", "B" , "C"]
print("after slicing:", fruits)

# pop()
removed_item = fruits.pop(2)
print(f"Removed item:", removed_item)
print("After pop()", fruits)

# remove
fruits.remove("C")
print("after remove('C'):", fruits)

# fruits.remove("D")
# print("after remove'D':", fruits)

idx = fruits.index("A")
print(idx)

item_to_remove = "Grapes"
if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")

else: 
    print("Insert a valid fruit...")