#create a class named as car
class car:
    #create method
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        print("This method is called")
        print(color, speed)

#create instances of class or objects
audi = car('black', 300)
bmw = car('blue', 350)
lamborgini = car('gray', 400)
