# ques 1 

class programmer():
    for i in range(11):
        name = input("Enter your name: ")
        branch = input("Enter your department: ")
        print("\n")

mayank = programmer()
print(mayank.name , mayank.branch)

# OR

class programmer:
    Company = "Microsoft"

    def __init__(self , name , salary , department):
        self.name = name
        self.salary = salary
        self.department = department

mayank = programmer("mayank" , 132468 , "AIML")
print(mayank.name , mayank.salary , mayank.department)

sweta = programmer("sweta", 2132456 , "Bio_medical")
print(sweta.name , sweta.salary , sweta.department)


# ques 2

class calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is: {self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n} is: {self.n**1/2}")

    def cube(self):
        print(f"The cube of {self.n} is: {self.n*self.n*self.n}")

a = calculator(4)
a.squareroot()
a.square()
a.cube()

# ques 3 

class exmaple:
    a = "mayank"

name = exmaple()
print(name.a)    # print the class attribute because the attribute is not changed yet 
name.a = 0       #instance attribute is sets 
print(name.a)     # print the instance attribute because it has more priority than the class one

# ques 4

class calculator:

    @staticmethod
    def greet():
        print("hellow!! \n")

    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is: {self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n} is: {self.n**1/2}")

    def cube(self):
        print(f"The cube of {self.n} is: {self.n*self.n*self.n}")

a = calculator(int(input("Enter the number: ")))
a.greet()
a.squareroot()
a.square()
a.cube()

# ques 5

from random import randint
class train:

    def __init__(slf , trainNo):
        slf.trainNo = trainNo

    def book(slf , fro , to):
        print(f"Your train is booked in ticket number: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train number {slf.trainNo} is running on time")

    def getFare(slf , fro , to):
        print(f"The fair of your train which is going to {fro} to {to} is: {randint(100 , 10000)}")

info = train(1928)
info.book("Delhi" , "Kolkatta")
info.getStatus()
info.getFare("Delhi" , "Kolkatta")

# ques 6

# from ques 5 we understand that any words can work as self 