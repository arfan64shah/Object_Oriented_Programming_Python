#declare class
class rectangle:
    pass

#instances of the class or objects
rect1 = rectangle()
rect2 = rectangle()

#declare attributes or variables for rect1 instance
rect1.length = 20
rect1.width = 10

#declare attributes or variables for rect1 instance
rect2.length = 30
rect2.width = 5

#area
area_rect1 = rect1.length * rect1.width
area_rect2 = rect2.length * rect2.width

print("Area of rectangle 1 is: ", area_rect1)
print("Area of rectangle 2 is: ", area_rect2)