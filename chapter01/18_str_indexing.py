message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

# message[0] = 'c'
# message = "New message"
print(f"Length of {message} = {len(message)}")

for char in message:
    print(char, end=" ")
print()

# enhanced for
for i in range(10 + 1):
    print(i)

print("----------------")
print(i)

# for imdexing based
message = "Coding Factory"

for i in range(len(message)):
    print(message[i], end=" ")

my_num = 123456789

# result: the addition of the 1st and the last digit -> 1 + 9 = 10
str_num = str(my_num)
first_num = int(str_num[0])
last_num = int(str_num[-1])

result = first_num + last_num           #na to skeytw sto spiti

print()
print(result)

print(f"result = {int(str_num[0]) + int(str_num[-1])}")

