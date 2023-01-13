class salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12 + self.bonus)

class employee:
    
    def __init__(self, fname, lname, salary):

        self.fname = fname
        self.lname = lname
        self.salary_obj = salary

    def total_salary(self):
        return self.salary_obj.annual_salary()


salary = salary(15000, 10000)
emp1 = employee("Arfan", "Shah", salary)

print(emp1.total_salary())

