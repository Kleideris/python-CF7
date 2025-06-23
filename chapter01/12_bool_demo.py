a = True
b = False

print(type(a), a, sep=", ")
print(type(b), b, sep=", ")

# Short circuit
result = a or b
print(result)

print("True + True =", True + True)     # Results in 2 because True has arithmetic value 1 (also False == 0)
print(True * 5)                         # So this results in 1 * 5 = 5