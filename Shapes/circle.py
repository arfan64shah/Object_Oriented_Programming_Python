# define a class named as polygon
from polygons import polygon
from shape import shape
import math

# define circle class
class circle(polygon, shape):
    # define function to find area
    def area(self):
        area = math.pi*self.get_radius()*self.get_radius()
        return area
    
    # define function to find circumference
    def circumference(self):
        circumference = 2*math.pi*self.get_radius()
        return circumference
    def color(self):
        return self.get_color()