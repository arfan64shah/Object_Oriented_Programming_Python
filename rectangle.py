from polygons import polygon
from shape import shape

class rectangle(polygon, shape):

    def area(self):
        area = self.get_length() * self.get_width()

        return area
    