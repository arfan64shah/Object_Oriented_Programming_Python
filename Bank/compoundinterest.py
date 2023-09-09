# import main info from main module
from main import mainInfo

# make a class for compound interest
class compoundInterest(mainInfo):
    
    # define a fuction for compound interest
    def comInterest(self):
        interest = self.get_depositMoney()*(1 + self.get_interestRate()/self.get_timelyCom())**(self.get_timelyCom()*self.get_time())
        return interest


