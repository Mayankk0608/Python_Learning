class college:
    institute = input("Enter your college name: ")
    university = input("Enter the university which belongs to your college: ")

    def campus(self):
        print(f"The name of the student is {self.institute} and the roll no. is {self.university}")

class name(college):
    name = input("Enter your name: ")
    roll_no = int(input("Enter your roll no.: "))

    def bio(self):
        print(f"The name and roll no. of student is {self.name}'{self.roll_no}'")

class batch(name):
    branch = input("Enter your branch: ")
    section = input("Enter your section: ")

    def department(self):
        print(f"The branch and section of {self.name} is {self.branch}{self.section}")

a = college()
b = name()
c = batch()
    
print("\n")
a.campus()
b.bio()
c.department()