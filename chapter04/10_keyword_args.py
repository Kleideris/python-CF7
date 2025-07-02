from typing import List, Tuple, Dict, Optional

# products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
# criteria = {"brand": "lenovo", "price": 100}

def get_results(products, **kwargs):
    """
    Filters a list of products baed on given keyword arguments.
    Each keyword argument corresponds to a product attribute.

    Params:
        products (ListTuple[str, int]): A list of tuples where each tuple contains a brand and a price.
        **kwargs(Dict[str, str | int]): Arbitrary keyword arguments for filtering.
    
    Returns:
        results (ListTuple[str, int]): Filtered list of our products.
    """
    results = [
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') >= price
    ]
    return results

def main():
    products = [("lenovo", 200), ("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()