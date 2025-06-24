#populate dict
#products = {1:"apple", 2:"banana", 3:"honey", 4:"melon"}

products = {
    1:"apple", 
    2:"banana", 
    3:"honey", 
    4:"melon"
}
print(f"Initial dict: {products}")

# insert/update a new key:value pair
products[3] = "orange"
print(f"Dict after insertion: {products}")

# read an element (access)
product_1 = products[1]
print("product_1: ", product_1)

# product_10 = products[10]  # will throw KeyError

product_1 = products.get(1)
print("product_1: ", product_1)

product_10 = products.get(10)
print("product_10: ", product_10)  # Will return None

product_10 = products.get(10, "Out of stock")
print("product_10: ", product_10)
