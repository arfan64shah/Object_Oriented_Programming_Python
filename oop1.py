import math

class shape:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

class rectangle(shape):
    def area(self):
        area = self.length*self.width
        return area

class square(shape):
    def area(self):
        area = math.pow(self.length, 2)
        return area

class circle(shape):
    def area(self):
        area = math.pi*math.pow(self.radius, 2)
        return area


rect_area = rectangle(4, 5, 6)
square_area = square(4, 5, 6)
circle_area = circle(4, 5, 6)

print("The area of rectangle is ", rect_area.area())
print("The area of square is ", square_area.area())
print("The area of circle is ", circle_area.area())