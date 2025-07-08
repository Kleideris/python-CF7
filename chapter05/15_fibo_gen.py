def fibo():
    a, b = 0, 1
    while True:  #TODO why do i need the while??
        yield a
        a, b = b, a + b

def main():
    fib = fibo()

    for i in range(10):
        print(f"Fib({i}) = {next(fib)}")
    
    fib = fibo()
    for num in fib:
        if num >= 100:
            break
        print(num)

    fib = fibo()
    fiblist = [next(fib) for _ in range(15)]
    print(fiblist)

if __name__ == "__main__":
    main()