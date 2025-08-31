import itertools

# for item in iterable:
#     names = ["mayank", "sweta", "chotu"]
#     for name in names:
#         print(name)

# for i in itertools.count(10,2):
#     print(i)
#     if i >= 30:
#         break

# THE MULTIPLICATION TABLE BY USING FOR LOOP
print("MULTIPLICATION TABLE BY USING FOR LOOP","\n")
n = int(input("Enter the no. for the multiplication table: "))
m = int(input("Enter the limit for the table: "))

print(f"\nMultiplication Table for {n} up to {m}:\n")

for i in range(1, m+1):
    print(f"{n} x {i} = {n*i}")

print("")
# WHILE LOOP 

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

print("MULTIPLICATION TABLE BY USING WHILE LOOP","\n")
n = int(input("Enter the no. for the multiplication table: "))
m = int(input("Enter the limit for the table: "))
# while m <= 1:
#     m +=1
print(f"\nMultiplication Table for {n} up to {m}:\n")

i = 1
while i <= m:
    # print(i)
    print(f"{n} x {i} = {n*i}")
    i += 1

print("")

