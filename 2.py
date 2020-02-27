print("")

"""
List1 = ["Item1", "Item22", "Item33", "AA", "BB"]

for i in List1:
 print(str(i) + "\t-\t" + str(len(i)))
print("")

for i in List1[0:2]:  # List1[0] and List1[1]
 print(str(i) + "\t-\t" + str(len(i)))
"""

# for i in range(0, 3):   # 0 through 2
# print(i)

# for i in range(0, 3, 1):
# print(i)

# for i in range(2, 4):
# print(i)

# for i in range(1, 10, 2):
# print(i)

# i = 1
# while i <= 10:
#  print(i)
#  i = i + 1


# i = 1
# while i <= 10:
#  if i == 5:
#   break
#  print(i)
#  i = i + 1


"""
i = 1
while i <= 10:
 if i == 5:
  i = i + 1
  continue
 print(i)
 i = i + 1
print("")

i = 0
while i < 10:
 i = i + 1
 if i == 5:
  continue
 print(i)
"""
List1 = [2, 4, 6]

for i in range(1, 21):
 if i in List1:
  continue
 print(str(i) + " is not in " + str(List1))
print("")