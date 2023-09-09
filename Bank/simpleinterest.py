# import the main module
from main import mainInfo

#now deine a class for simple interest
class simpleInterest(mainInfo):
    
    # define a function for calculation of simple interest
    def simInterest(self):
        interest = self.get_depositMoney()*self.get_interestRate()*self.get_time()
        return interest
        