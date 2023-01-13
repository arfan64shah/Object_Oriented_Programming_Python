import polygons
import shape

class rectangle(polygons, shape):

    def area(self):
        area = self.get_length * self.get_width

        return area
    