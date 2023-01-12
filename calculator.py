class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class add(calculator):
    def addition(self):
        add = self.num1+self.num2
        return add

class subtract(calculator):
    def sub(self):
        sub = self.num1 - self.num2
        return sub

class multiply(calculator):
    def multi(self):
        product = self.num1*self.num2
        return product

class division(calculator):
    def divide(self):
        divide = self.num1/self.num2
        return divide

# num1 = int(input())
# num2 = int(input())
# print("Enter first number:", num1)
# print("Enter second number: ", num2)


addition = add(5, 6)
subtraction = subtract(5, 6)
multiplication = multiply(5, 6)
div = division(5, 6)

print("The sum of entered numbers is ", addition.addition())
print("The subtraction of entered numbers is ", subtraction.sub())
print("The multiplication of entered numbers is ", multiplication.multi())
print("The division of entered numbers is ", div.divide())
