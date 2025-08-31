
# INHERITANCE CLASS 
# class employee:   # base class or parent class 
#     company = "ITC"

#     def show(self):
#         print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")

# class programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")

#     def languaage(self):
#         print(f"The name of employee is {self.name} and the language of employee is {self.language}")

# class programmer(employee):    # derived class or child class
#     company = "ITC infotech"

#     def language(self):
#         print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")

# a = employee
# b = programmer
# print(a.company , b.company)

# MULTIPLE INHERITANCE CLASS 

# class employee:   # base class or parent class 
#     company = "ITC"
#     name = "mayank"
#     def show(self):
#         print(f"The name of employee is {self.name} and the company of employee is {self.company}")

# class coder:
#     lang = "python"
#     def printlanguage(self):
#         print(f"the language with the most given votes is {self.lang}") 

# class programmer(employee , coder):    # derived class or child class
#     company = "ITC infotech"
#     def programmerself(self):
#         print(f"The name of employee is {self.name} and the languauge of employee is {self.lang}")

# a = employee()
# b = programmer()
# # print(a.company , b.company)

# b.show()
# b.programmerself()
# b.printlanguage()

# MULTILEVEL INHERITANCE CLASS                 #SUPER METHOD

# class employee:
#     def __init__(self):
#         print("This belongs to employee")
#     name = "mayank"

# class programmer(employee):
#     def __init__(self):
#         print("This belongs to programmer")
#     company = "ITC"

# class language(programmer):
#     def __init__(self):
#         super().__init__()    # returns the constructor of its parent class even when its no called
#         print("This belongs to language")
#     language = "javascript"

# o = employee()
# print(o.name)

# k = programmer()
# print(k.name , k.company)

# m = language()
# print(m.name , m.company , m.language)



# MULTI INHERITANCE CLASS Example_2

# class campus:
#     college = "GLBAJAJ"
#     institute = "AKTU"

#     def name(self):
#         print(f"The name of the clg is {self.college} and the university of this clg is {self.institute}")

# class student(campus):
#     name = "mayank"
#     roll_no = 2135051219

#     def selfName(self):
#         print(f"The name of the student is {self.name} who studied in {self.college} and his institute is {self.institute}")

#     def selfRoll_No(self):
#         print(f"The roll no of student is: {self.roll_no}")

# class batch(student):
#     batch = "AIML"

#     def department(self):
#         print(f"The department of student is {self.batch}")

# o = campus()
# # print(o.college)
# # print(o.selfName , o.roll_no)
# a = student()
# k = batch()

# o.name()
# a.selfName()
# a.selfRoll_No()
# k.department()

# class methods

# class Employee:
#     name = "Mayank"

#     @classmethod
#     def Name(cls):
#         print(f"The name in class attribute is: {cls.name}")

# e = Employee()
# e.name = "sweta"

# e.Name()

# property decorators 

class Employee:
    roll_no = 2135051219

    @classmethod
    def roll_No(cls):
        print(f"The roll_no in class attribute is: {cls.roll_no}")

    @property
    def full_Name(self):
        return (f"{self.f_Name} {self.l_Name}")
    
    @full_Name.setter
    def full_Name(self , value):
        self.f_Name = value.split(" ")[0]
        self.l_Name = value.split(" ")[1]

e = Employee()
e.roll_no = 21350512212
e.full_Name = input("Enter your name: ")

print(e.f_Name)
e.roll_No()