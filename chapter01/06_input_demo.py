name = input("please insert you name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height: "))

is_student = input("Are you a student? (Yes/No): ").lower() == "yes"  # (YES yES, YeS,yes)

print(f"Hello {name}!")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

print("your age is {} and your height is {:.2f} meters".format(age, height))