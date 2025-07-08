class FactoIterator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        self.n = n
        self.result = 1
        self.order = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result
    
def main():
    facto_iter = FactoIterator(10)

    # get the first factorial using next() func
    a = next(facto_iter)
    print(a)
    print("---")

    for facto in facto_iter:
        print(facto)
    print("---------")

    new_facto_iter = FactoIterator(5)
    for index, factorial in enumerate(new_facto_iter, start=1):
        print(f"Factorial of {index} = {factorial}")
    
    #TODO na skeutw pws ksepernaw ton periorismo tou oti kathe kainourio facto ksekinaei apo thn arxh.

if __name__ == "__main__":
    main()