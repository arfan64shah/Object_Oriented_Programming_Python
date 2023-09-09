# make a class to get general info
class mainInfo:
    __fName = None
    __lName = None
    __fatherName = None
    __cnic = None
    __gmail = None
    __phone = None
    __depositMoney = None
    __interestRate = None
    __time = None
    __timelyCom = None
    
    # general info storing function
    def set_Simvalues(self, depositMoney, interestRate, time):
        self.__depositMoney = depositMoney
        self.__interestRate = interestRate
        self.__time = time
    def set_Comvalues(self, depositMoney, interestRate, time, timelyCom):
        self.__depositMoney = depositMoney
        self.__interestRate = interestRate
        self.__time = time
        self.__timelyCom = timelyCom
    
    # write functions for getting the private variables
    def get_depositMoney(self):
        return self.__depositMoney
    def get_interestRate(self):
        return self.__interestRate
    def get_time(self):
        return self.__time
    def get_timelyCom(self):
        return self.__timelyCom
        
        
    
        

        
    

        