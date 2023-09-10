# declare a class
class shape:
    # declare variables
    __color = None
    # define a function
    def set_color(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
    