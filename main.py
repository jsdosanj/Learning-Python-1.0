import Module1
# import Module1 as Utilities
import random

# Module1.f1()
# Module1.f2()

# Utilities.f1()  # if you use import Module1 as Utilities
# Utilities.f2()  # if you use import Module1 as Utilities

# Number = random.randrange(1, 10) # This will generate a random number form 1 to 9
# print("Your random number is: " + str(Number))


for i in range(1, 11):
 Number = random.randrange(1, 1001)
 print("Attempt number " + str(i) + ": your random number is: " + str(Number))

