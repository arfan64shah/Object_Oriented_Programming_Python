# import required modules
from simpleinterest import simpleInterest
from compoundinterest import compoundInterest

# instances for simple and compund interest
simInt = simpleInterest()
comInt = compoundInterest()

# set values
simInt.set_Simvalues(1000, 0.15, 3)
comInt.set_Comvalues(1000, 0.15, 3, 2)

print("Simple interest is ", simInt.simInterest())
print("Compound interest is ", comInt.comInterest())