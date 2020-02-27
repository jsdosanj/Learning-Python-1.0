print("\n### Sets ###\n")

# A set is an unordered and unindexed collection of items
# Sets don't allow duplicate values.

Set1 = {"Item1", "Item2", "Item3", "Item1"}

print(Set1)
print("Item1" in Set1)

if "Item1" in Set1:
 print("Exists")

if "Item11" not in Set1:
 print("Doesn't Exist.")

for item in Set1:
 print(item)



print("")
