# Falsy - Truthy Values
# Falsy: 0, 0.0, 0j -> for imaginary numbers, "", [], (), {}, set(), False, None
# Truthy: everything else

empty_dict = {}  # defines an ampty dict! Not a set.
print(type(empty_dict))

a = 5

if a > 0 and a < 10:
    print("valid number")

if 0 < a < 10:
    print("Valid number")