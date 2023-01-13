from polygons import polygon
from shape import shape

class triangle(polygon, shape):

    def area(self):
        area = (self.get_length()*self.get_width())/2

        return area
