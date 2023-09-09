#define a polygon class
class polygon:
    __width = None
    __length = None
    
    # define a function to set values
    def set_values(self, width, length):
        self.__width = width
        self.__length = length
    
    #define another function to get width
    def get_width(self):
        return self.__width
    
    # define next function for getting length
    def get_length(self):
        return self.__length
    
 #another class for triangle   
class triangle(polygon):
    
    # define a function for area
    def area(self):
        return (self.get_width()*self.get_length())/2

#define another class for rectangle
class rectangle(polygon):
    # define function for area
    def area(self):
        return self.get_width()*self.get_length()

# make objects for rectangle and triangle
rect = rectangle()
tri = triangle()

# set values
rect.set_values(10, 5)
tri.set_values(20, 10)

#area
print("The area of Rectangle is ", rect.area())
print("The area of Triangle is ", tri.area())

    