# range(10)

a = range(10)
print(f"Type of a: {type(a)}")

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()
print("-" * 10)

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("Loop ended normally")

for i in range(10):
    if i == 100:
        break
    print(i, end=" ")
else:
    print("Loop ended normally")

# List of fruit
fruits = ["Banana", "Orange", "Mango", "Grapes"]

fruit_to_check = "Banana"

#that is java style
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in list")
        break
else:
    print(f"{fruit_to_check} not in list")

# Happy hour
print("Why do python devs never get lost?")
print("Because they always know where 'in' is!")

# this is how its done in python
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in list")
else:
    print(f"{fruit_to_check} not in list")

# challenge
print("one line exe")
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} list!!")

# questionable variation to rethink your carrer choices
print(f"{fruit_to_check} is {"not " * (fruit_to_check not in fruits)}in the list!?!")

