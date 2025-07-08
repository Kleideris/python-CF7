class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self): #TODO na dw ti kanei auto
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index] #TODO na to ksanadw
            self.index += 1
            return result
        else:
            raise StopIteration

def main():
    numbers = [10, 20, 30, 40, 50]

    # create an instance of SimpleIterator (an iterator)
    my_iter = SimpleIterator(numbers)

    a = next(my_iter)
    print(a)
    print("--------------------")
    for item in my_iter:
        print(item)


if __name__ == "__main__":
    main()