import math

class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1
        
    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
        

    def distance_from_center(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __lt__(self, other):
        return self.distance_from_center() < other.distance_from_center()
    
    def __gt__(self,other):
        return self.distance_from_center() > other.distance_from_center()
    
    def __le__(self, other):
        return self.distance_from_center() <= other.distance_from_center()
    
    def __ge__(self, other):
        return self.distance_from_center() >= other.distance_from_center()

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

def main():
    p1 = Point(11, 20)
    p2 = Point(10, 20)
    print(p1)
    print(p2)
    p1.x = 10
    print(p1.x, p1.y)
    print(f"p1  == p2: {p1 == p2}")
    print(Point.get_count)

    print("------------------")
    print("p1 distance from center: ", p1.distance_from_center()) #TEST
    print("p2 distance from center: ", p2.distance_from_center()) #TEST
    print("p1 < p2: ", p1 > p2)



if __name__ == "__main__":
    main()