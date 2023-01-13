class polygon:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

class rectangle(polygon):
    def area(self):
        return self.get_length() * self.get_width()

class triangle(polygon):
    
    def area(self):
        return (self.get_length() * self.get_width())/2

rect = rectangle(10, 12)
tria = triangle(10, 12)

print("The area of Rectangle is ", rect.area())
print("The area of Triangle is ", tria.area())