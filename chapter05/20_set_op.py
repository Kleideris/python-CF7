def main():
    store_a_products = {"Apples", "Bananas", "Cherries", "Watermelons",}
    store_b_products = {"Bananas", "Cherries", "Figs","Grapes", "Melons"}

    # Find common products (intersection) availiable in both stores
    common_products = store_a_products & store_b_products
    print("common products:",common_products)
    # alternatively
    common_products2 = store_a_products.intersection(store_b_products)
    print("common products2:",common_products2)

    # Find all unique products (union) across both stores (A and B)
    all_products = store_a_products | store_b_products
    print("all products:",all_products)
    # using func
    all_products = store_a_products.union(store_b_products)
    print("all products:",all_products)

    # Find products availiable in store B but not in store A (difference)
    store_b_exclusive = store_b_products - store_a_products
    print("store b exclusive:", store_b_exclusive)

    # using function
    store_b_exclusive2 = store_b_exclusive.difference(store_a_products)
    print("store b exclusive2:", store_b_exclusive2)

    # Find products that are in either store A or store B but not in both
    unique_to_either_store = store_a_products ^ store_b_products
    print("Unique to either store", unique_to_either_store)
    # using func
    unique_to_either_store2 = store_a_products.symmetric_difference(store_b_products)
    print("Unique to either store2", unique_to_either_store2)

if __name__ == "__main__":
    main()