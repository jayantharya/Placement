class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h
shapes = [Circle(5), Rectangle(4, 6), Triangle(4,6)]
for s in shapes:
    print(f"Area: {s.area()}")