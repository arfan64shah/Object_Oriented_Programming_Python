# build a class for salary
class salary:
    pay = None
    bonus = None
    
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_salary(self):
        return 12*self.pay+self.bonus

# another class for employee
class employee:
    name = None
    age = None
    
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        
        # create an object for composition
        self.obj_salary = salary(pay, bonus)
        
    def total_salary(self):
        return self.obj_salary.annual_salary()
    
emp = employee("Arfan", 23, 300000, 1000000)

print(emp.total_salary())
        
         
    