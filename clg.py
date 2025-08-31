import random

# num = [3,4,5,6,7]

# num.append(False)
# num.append(True)
# print(num)

# num.remove(4)
# print(num)

# num.clear()
# print(num)


# RANDOM IS THE PACKAGE IN THE PYTHON TO GENERATE RANDOM VARIABLE 

#returns random variable
# h = random.choice(3,4,5,6,7)
# print(h)

# print(10/3)
# print(10/2) #returns value in decimal part
# print(10//2) #returns the value in integer part


# new =(6,7,4,7,9)
# print(new)
# print(type(new))

# tuple =(1,2,3,4)
# mytuple =('a','b','c','d')
# a,b,c,d = mytuple
# print(a,b,c,d)

choice = ["snake", "water", "gun"]
computer = random.choices(choice)
computer_choice = ''.join(computer)
print(computer_choice)