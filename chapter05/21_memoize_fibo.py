def memoize(func):
    """
    A simple memoization decorator to cache results of the function.
    """
    #TODO na skeytw an ginete me sets kai unions
    #TODO na dw posos xronos swthhke
    #TODO na kanw cahce ta hits
    #TODO na dw pws tha epistrepsw to cache_stats

    cache = {}
    cache_stats = {"hits": 0, "misses": 0}

    def wrapper(n):
        if n in cache:
            cache_stats["hits"] += 1 
            print(f"Cache hit for fibo({n})")
        else:
            cache_stats["misses"] += 1 

            print(f"Calculating Fibo({n})")
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1 :return n
    else: return fibonacci(n-1) + fibonacci(n-2)

def main():
    print([fibonacci(n) for n in range(10)])

if __name__ == "__main__":
    main()