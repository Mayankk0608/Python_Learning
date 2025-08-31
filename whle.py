# ques 1 

m = int(input("enter the no. for multiplication table: "))
n = int(input("enter the no. for for length of the table: "))

print(f"\nthe multiplication table of {m} up to {n} are: ")
for i in range(1,n+1):
    print(f"{m} x {i} = {m*i}")

# ques 2 

l = ["harry","rohan","sweta","mayank"]

for i in l:
    if i.startswith(("s")):
        print(f"hello {i}")

i = 1
while i<=n:
    print(f"{m} x {i} = {m*i}")
    i+=1

num = int(input("enter the no. u want to check whether its prime no. or not: "))

for i in range(2,num):
    if num%i == 0:
        print("its not a prime no.")
        break

else:
    print("its a prime no.")

natural = int(input("enter the no. u want to check whether its prime no. or not: "))

i = 1
sum = 0
while (i <= natural):
    sum += i
    i+= 1
print(f"the sum of first {natural} natural no. is: {sum}")

fact = int(input("enter the no. for finding its factorial: "))
product = 1
for i in range(1, fact+1):
    product = product * i
print(f"factorial of {fact} is: {product}")


n = 5

for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()

n = int(input("enter no. for star: "))

for i in range(1,n+1):
    print(" "* (n-i),end='')
    print("*"* (2*i-1),end='')
    print("")

k = int(input("Enter tha no. of stars: "))
for t in range(k):
    for j in range(t+1):
        print("*",end='')
    print()

h = int(input("Enter the no. of stars: "))
for k in range(1,h+1):
    if k == 1 or k == h:
       print("*"* h,end='')

    else:
        print("*",end='')
        print(" "* (h-2),end='')
        print("*",end='')
    print("")

mul = int(input("enter no. for reversed multiplication table: "))
for i in range(1,11):
    print(f"{mul} x {11-i} = {mul*11-i}")

def factorial(n):
    result = 1
    for i in range(1 , n+1):
        result *= i
    return result

fact = int(input("enter the number for factorial: "))
print(factorial(fact))

n = int(input("enter how many times u want to print this: "))
for i in range(1 , n+1):
    print("sweta")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n*factorial(n-1)
    
fact = int(input("enter the number for factorial: "))
print(factorial(fact))

