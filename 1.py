print("")

# Arithmetic Operators:
#----------------------
# <
# <=
# >
# >=
# ==
# !=

"""
x = 10
if x == 10:
 print("x = " + str(x))

if x != 1000:
 print("x != 1000")

if x <= 10:
 print("x <= 10")
else:
 print("x > 10")

if x < 10:
 print("x < 10")
elif x > 10:
 print("x > 10")
else:
 print("x = 10")
"""

# x = 10
# print("x < 10") if x < 10 else print("x >= 10")
# print("x < 10") if x < 10 else print("x > 10") if x > 10 else print("x = 10")

'''
x = "Test"
if x == "Test":
 print("x = \a\"Test\"")
else:
 print("x != \"Test\"")
'''

"""
x = 1
y = 2
if x == 1 and y == 2:
 print("x = 1 and y = 2")

if x == 1 or y == 3:
 print("x = 1 or y = 3")
"""

"""
x = 10
y = -2

if x == 1:
 print("x = 1")
 if y < 0:
  print("y is a negative numebr.")
 else:
  print("y is a positive numebr.")
else:
 print("x != 1")
"""

"""
x = 1

if x == 1:
 pass

print("after pass")
"""

SearchFor = 100
List1 = [10, 20, 30]

if SearchFor in List1:
 print(str(SearchFor) + " is in " + str(List1))
else:
 print(str(SearchFor) + " is not in " + str(List1))

print("")




# 1. Jack's dictionary 
jack = { "name":"Jack Frost", 
		"assignment" : [80, 50, 40, 20], 
		"test" : [75, 75], 
		"lab" : [78.20, 77.20] 
	} 
		
# 2. James's dictionary 
james = { "name":"James Potter", 
		"assignment" : [82, 56, 44, 30], 
		"test" : [80, 80], 
		"lab" : [67.90, 78.72] 
		} 

# 3. Dylan's dictionary 
dylan = { "name" : "Dylan Rhodes", 
		"assignment" : [77, 82, 23, 39], 
		"test" : [78, 77], 
		"lab" : [80, 80] 
		} 
		
# 4. Jessica's dictionary 
jess = { "name" : "Jessica Stone", 
		"assignment" : [67, 55, 77, 21], 
		"test" : [40, 50], 
		"lab" : [69, 44.56] 
	} 
		
# 5. Tom's dictionary 
tom = { "name" : "Tom Hanks", 
		"assignment" : [29, 89, 60, 56], 
		"test" : [65, 56], 
		"lab" : [50, 40.6] 
	} 


for num in list:
    sum = sum +num
average  = sum / len(list)
print ("sum of list element is : ", sum)



# Function calculates average 
def get_average(marks): 
	total_sum = sum(marks) 
	return total_sum

# Function calculates total average 
def calculate_total_average(students): 
	assignment = get_average(students["assignment"]) 
	test = get_average(students["test"]) 
	lab = get_average(students["lab"]) 

# Function to calculate the total 
# average marks of the whole class 
def class_average_is(student_list): 
	result_list = [] 

	for student in student_list: 
		stud_avg = calculate_total_average(student) 
		result_list.append(stud_avg) 
		return get_average(result_list) 

# Student list consisting the 
# dictionary of all students 
students = [jack, james, dylan, jess, tom] 

# Iterate through the students list 
# and calculate their respective 
# average marks and letter grade 
for i in students : 
	print(i["name"]) 
	print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
	print("Average marks of %s is : %s " %(i["name"], 
						calculate_total_average(i))) 
	print() 


# Calculate the average of whole class 
class_av = class_average_is(students) 
print( "Class Average is %s" %(class_av)) 

