import math

m = int(input("Enter the no. for factorial: "))
n = math.factorial(m)
print(f"The factorial of {m} is: {n}")

def add(a,b):
    return (a + b)

print(add(5,5))
print(add(65,76))

def calculate_area(radius):
    return 3.14 * radius ** 2

r=5
print(f"Area: {calculate_area(r)}")

def multiply_by_two(x):
    return x * 2

print(multiply_by_two(int(input("Enter the no.: "))))  # Output: 10
print(multiply_by_two(int(input("Enter the no.: "))))  # Output: 20


def multiplication(p,q):
    return p * q

p = int(input("enter value 1: "))
q = int(input("enter value 2: "))

print(multiplication(p,q))

