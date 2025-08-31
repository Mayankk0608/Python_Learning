# file reading 
f = open("file.txt")
data = f.read()
print(data)
f.close()

# file writing
name = "my name is mayank"
k = open("myFile.txt" , "w")
k.write(name)
k.close()

# file multi lines raeding
f = open("file_reading.txt")

# for printing only single line from file
lines = f.readline()
lines_1 = ''.join(lines)
print(lines_1)
lines = f.readline()
lines_2 = ''.join(lines)
print(lines_2)

# for printing multi lines at onces
lines = f.readlines()
lines_3 = ''.join(lines)
print(lines_3)

line = f.readline()
while line != "":
    print(line) 
    line = f.readline()
f.close()

for i in line:
    print(line)
    line = f.readline()
f.close()

# appending the sentence at the end of a file 
para = "That's the best thing i can do "
f = open("myFile.txt" , "a")
f.write(para)
f.close()

# use of with statement: isme close function use nhi hoga
with open("file_reading.txt") as f:
    print(f.read())

# one day I'll win that fucking hackathon...