#create a class named as car
class car:
    #create method
    def __init__(self, color, speed):
        self.__color = color
        self.__speed = speed
        #print("This method is called")
        #print(color, speed)
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
        

#create instances of class or objects
audi = car('black', 300)
bmw = car('blue', 350)
lamborgini = car('gray', 400)

print(audi.get_color(), audi.get_speed())
print(bmw.get_color(), bmw.get_speed())
print(lamborgini.get_color(), lamborgini.get_speed())

