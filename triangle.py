import polygons
import shape

class triangle(polygons, shape):

    def area(self):
        area = (self.get_length*self.width)/2

        return area