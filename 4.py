print("")

"""
a = 1 # Global Variable

def f1():
 print(a)

def f2():
 print(a)

f1()
f2()
"""

"""
a = 1 # Global Variable

def f1():
 a = 1000  # Local variable
 print(a)

def f2():
 print(a)

f1()
f2()
"""

"""
def f3(x = 1, y = 2, z = "Test"):
 print("x = " + str(x)) 
 print("y = " + str(y))
 print("z = " + str(z))
 

# f3(10, 20, "NewTest")
# f3(x = 10, y = 20, z = "NewTest")
# f3(y = 222, x = 111, z = "NewTest")
# f3(y = 222, x = 111)
# f3(x = 111)
f3()
"""

"""
def f4(*args):
 Sum = 0
 for arg in args:
  #print(arg)
  Sum = Sum + arg
 print("args has " + str(len(args)) + " arguments.")
 return Sum
 


Sum = 0
Sum = f4(1);             print(str(Sum) + "\n")
Sum = f4(1, 2, 3);       print(str(Sum) + "\n")
Sum = f4(1, 2, 3, 4, 5); print(str(Sum) + "\n")
"""




def f5(x, y, z):
 print("x = " + str(x))
 print("y = " + str(y))
 print("z = " + str(z))

f5(100, 200, 300)
print("")

List1 = [100, 200, 300]
f5(*List1)
print("")


f5(List1[0], List1[1], List1[2])
































print("")