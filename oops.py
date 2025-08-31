# BASIC SYNTAX FOR CREATING A CLASS 
class Employee():
    name = "mayank"   # This is a class attribute
    branch = "AIML"
    salaray = 1234567890

    # CONSTRUCTOR
    def __init__(self , name , branch , salary):  #that's called as dunder method which called automatically without mentioning it
        self.name = name 
        self.branch = branch
        self.salaray = salary
        print("bio data of employee")

    def getInfo(self):
        print(f"The name of student is {self.name}, of the branch {self.branch} aiming the salary of {self.salaray}")

    @staticmethod
    def greet():
        print("Good Morning !")

intro = Employee("mayank" , "AIML" , 7625334564)
# intro.place = "Delhi"   # This is a instance attribute
# intro.name = "sweta"    # The instance attribtues re-werites from the class attributes
# print(intro.name , intro.branch , intro.place)
# intro.greet()
# intro.getInfo()
print(intro.branch , intro.salaray , intro.name)