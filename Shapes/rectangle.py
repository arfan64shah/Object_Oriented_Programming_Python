# import required modules
from polygons import polygon
from shape import shape

# define a rectangle class
class rectangle(polygon, shape):
    # write a function for area
    def area(self):
        area = self.get_width()*self.get_length()
        return area
    
    # define a function for circumference
    def circumference(self):
        circumference = 2*(self.get_width()*self.get_length())
        return circumference
    
    def color(self):
        return self.get_color()