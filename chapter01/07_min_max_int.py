import sys

max_int = sys.maxsize
print("Max int for 64-bit system:", max_int)

min_int = -sys.maxsize -1
print("Min int for 64-bit system:", min_int)

# 64-bit
# Max int: 9223372036854775807
# Min int: -9223372036854775808

print("-" * 40)

# for a 32 bit system it would be:
max_int = sys.maxsize // (2 ** 32)
min_int = -sys.maxsize // (2 ** 32)             # there is no -1 here because this devision has a remainder in binary
                                                # and  // rounds toward the negative infinity and not 0
print("Max int for 32-bit system:", max_int)
print("Min int for 32-bit system:", min_int)

# 32-bit
# Max int: 2147483647
# Min int: -2147483648
