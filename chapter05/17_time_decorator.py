import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a funtion.
    
    Params:
        func (function): The function to be decorated.
    
    Returns:
        function: The decorated function with added timing functionality.
    """
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # execution
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    
    return inner_function

def sum_function(n):
    return sum(range(n))

print(sum_function(1_000_000))
print("--------------\n")

my_sum_func = timer_decorator(sum_function)
print(my_sum_func(1_000_000))
print("--------------\n")


# otan xrhsimopoiw decorator den allazei to onoma ths synarthshs giati ginetai auto sthn ousia.
# sum_func = timer_decorator(sum_function)
# print(my_sum_func(1_000_000))

# Decorators
@timer_decorator
def average_function(n):
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_function(101))


#TODO what makes a def a decorator