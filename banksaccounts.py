class basicinfo:

    __fname = None
    __lname = None
    __acc_no = None
    __cinic_no = None
    __amount = None
    __profit = None
    __cust_no = None

    def __init__(self, fname, lname, cust_no, acc__no, cnic_no, amount):
        self.__fname = fname
        self.__lname = lname
        self.__acc_no = acc__no
        self.__cinic_no = cnic_no
        self.__amount = amount
        self.__cust_no = cust_no


    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def cust_no(self):
        return self.__cust_no

    def get_acc_no(self):
        return self.__acc_no

    def get_cnic_no(self):
        return self.__cinic_no

    def get_amount(self):
        return self.__amount

    def get_profit(self):
        self.__profit = 0.2 * self.__amount
        return self.__profit

customer1 = basicinfo("Arfan", "Shah", 1, 12345, 7140122456920, 150000)
# customer2 = basicinfo()
# customer3 = basicinfo()
# customer4 = basicinfo()
# customer5 = basicinfo()

print("The profit for the customer no " + str(customer1.cust_no()) + " is " + str(customer1.get_profit()))