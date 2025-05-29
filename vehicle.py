# import required libraries

# define a parent class
class vehicle:
    
    # define a method
    def general_usage(self):
        print("The general usage of vehicle is for transportation!")

class car(vehicle):
    def __init__(self, tyres, transport_type):
        self.tyres = tyres
        self.transport_type = transport_type
    def tyre(self):
        print("Number of tyres in this vehicle are", self.tyres)
    
    def transport(self):
        print(self.transport_type, "is used for family events!")

class motor_byke():
