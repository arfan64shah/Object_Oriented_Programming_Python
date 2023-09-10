# define the 
class polygon:
    # declare null variables
    __width = None
    __length = None
    __radius = None
    
    # set values for circle
    def set_valCir(self, radius):
        self.__radius = radius
    # set values for rectangle
    def set_values(self, width, length):
        self.__width = width
        self.__length = length
        
    # get values using functions as the variables are private
    def get_width(self):
        return self.__width
    def get_length(self):
        return self.__length
    def get_radius(self):
        return self.__radius