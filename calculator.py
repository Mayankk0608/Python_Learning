import pyttsx3
engine = pyttsx3.init()

a= float(input("Enter first no. : "))
b= float(input("Enter second no. : "))

print("")
print("select any number from 1 to 5:")

print(""" 1. ADDITION
 2. SUBTRACTION
 3. MULTIPLICATION
 4. DIVISION
 5. MODULATION """)

engine.say("select any number from 1 to 5:")
engine.runAndWait()

print("")

c = float(input("select a number :"))
# a= float(a)
# b= float(b)
# c= float(c)

if c == 1 :
    print(" the addition of a and b is :", a+b)
    engine.say(" the addition of a and b is : ", a+b)
    engine.say(a+b)
    engine.runAndWait()

elif c == 2 :
    print(" the subtraction of a and b is :", a-b)
    engine.say(" the subtraction of a and b is : ", a-b)
    engine.say(a-b)
    engine.runAndWait() 

elif c == 3 :
    print(" the multiplication of a and b is :", a*b)
    engine.say(" the multiplication of a and b is : ", a*b)
    engine.say(a*b)
    engine.runAndWait()

elif c == 4 :  
    print(" the division of a and b is :", a/b)
    engine.say(" the division of a and b is : ", a/b)
    engine.say(a/b)
    engine.runAndWait()

elif c == 5 :
    print(" the modulation of a and b is :", a%b)
    engine.say(" the modulation of a and b is : ", a%b)
    engine.say(a%b)
    engine.runAndWait()

else:
    print("u can choose only from 1,2,3,4,5")
    engine.say("u can choose only from 1 2 3 4 5")
    engine.runAndWait()