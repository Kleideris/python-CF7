class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self.__y = y
        
    def __str__(self):
        return f"({self._x}, {self.__y})"

def main():
    p1 = Point(11, 20)
    print(p1)

    print(p1._x)
    p1.__y = 100  # this can be printed because with this line of code we are creating dynamically a new variable __y (which does not exist in our class) and assigning it the value 100
    
    # print(p1._Point__y)


if __name__ == "__main__":
    main()