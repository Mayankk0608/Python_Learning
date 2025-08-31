# function defination
def add():
    a = int(input("First number: "))
    b = int(input("second number: "))
    print(a+b)

# function call
add()

def greet(name , ending ):
    # name = input("whats ur name? ")
    # print(f"good evening {name}")
    print("good evening " + name)
    print(ending)
    print("")

greet("mayank" , "thank u")
greet("sweta" , "thank u")
greet("chotu" , "thank u")

def addition(a,b):
    return a+b

print(addition(5,6))

def multiplication():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a*b

times = int(input("how many times u want to call this fuction: "))
print("")
# h = multiplication()
for i in range(1,times+1):
    print(multiplication())