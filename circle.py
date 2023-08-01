import math
#initiate class circle
class circle:
    #initiate a function which serves a constructor
    def __init__(self, radius):
        self.radius = radius
    #initiate another function for area
    def area(self):
        return (self.radius**2)*math.pi
circle1 = circle(5)
print(circle1.area())

#initiate another class
class rectangle:
    #initiate a function which serves as a constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
#delcare instances of rectangle
rect1 = rectangle(10, 5)
rect2 = rectangle(20, 15)

print("The area of triangle 1 is ", rect1.area())
print("The area of triangle 2 is ", rect2.area())