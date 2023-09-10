# import the required modules
from circle import circle
from rectangle import rectangle

# make instances of circle and rectangle
circle = circle()
rect = rectangle()

# set values in the set functions
circle.set_valCir(5)
rect.set_values(5, 10)
circle.set_color('Red')

# print area and circumference
print("The area of the cricle is ", circle.area())
print("The circumference of the circle is ", circle.circumference())
print("The area of the rectangle is ", rect.area())
print("The circumference of the rectangle is ", rect.circumference())

print("The color of circle is ", circle.color())