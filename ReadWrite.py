FileName     = "./Files/File1.txt"
Contents_str = ""


# FileWrite = open(FileName, "a") # a -> append
FileWrite = open(FileName, "w") # w -> write
FileWrite.write("Line1\n")
FileWrite.write("\n")
FileWrite.write("\n")
FileWrite.write("Line2\n")
FileWrite.write("\n")
FileWrite.write("\n")
FileWrite.close()


FileRead = open(FileName, "r")  # r -> read
Contents_str = FileRead.read()
FileRead.close()

print(Contents_str)
print("There are " + str(len(Contents_str)) + " characters in " + FileName + ".")


Lines = Contents_str.split("\n")
for Line in Lines:
 if len(Line) > 0:
  print(Line)

print("\n###############\n")

FileRead = open("./Files/File1.txt", "r")
Line = FileRead.readline();
Line = Line[0:len(Line) - 1] # Get rid of "\n"
print(Line)

Line = FileRead.readline();
Line = Line[0:len(Line) - 1] # Get rid of "\n"
print(Line)

FileRead.close()

print("\n###############\n")

FileRead = open(FileName, "r")

Line = FileRead.readline()
while(Line):
 if len(Line) > 1:             # If the file is not empty ("\n")
  Line = Line[0:len(Line) - 1] # Get rid of the trailing "\n"
  print(Line)
 Line = FileRead.readline()

FileRead.close()

print("\n###############\n")

FileRead = open(FileName, "r")
Lines = FileRead.readlines()
for Line in Lines:
 if len(Line) > 1:
  Line = Line[0:len(Line) - 1]
  print(Line)

FileRead.close()


print("Therer are " + str(len(Lines)) + " lines in " + FileName + ".")


























