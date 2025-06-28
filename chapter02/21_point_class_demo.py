import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y coordinate of thr point.
    """

    def __init__(self, x: float = 0, y: float = 0):
        """
        Initialize a Point object with specified x and y coordinates.

        Args:
            x (float): The x-coordinate of the point. Defaults to 0.
            y (float): The y coordinate of thr point. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
    
def main():
    p1 = Point(3, 0)
    p2 = Point(0, 4)

    print(f"p1: {p1}")
    print(f"p2: {p2}")

    print(f"distance: {p1.distance_to(p2)}")

if __name__ == "__main__":
    main()

    