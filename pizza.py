# size = regular{100} , medium{120} and large{140} 
# user select krega ki ktina base hoga = 3 thick =90 medium = 70 thin = 60
# extra cheese or regular ? extra = 80 regular = 50 

size_regular = 100
size_medium = 120
size_large = 140

base_thin = 60
base_medium = 70
base_thick = 90

regular_cheese = 50
extra_cheese = 80

print("""choose the size for ur pizza:
Enter 'R' for regular 
Enter 'M' for medium 
Enter 'L' for large\n""")
s = input("Enter the size for pizza:").upper()
print("\n")

print("""choose the base for ur pizza:
Enter 'T' for regular 
Enter 'A' for medium 
Enter 'D' for large\n""")
b = input("Enter the base for pizza:").upper()
print("\n")

print("""choose cheese for ur pizza:
Enter 'E' for extra cheese
Enter 'C' for regular cheese\n""")
ch = input("Enter the base for pizza:").upper()
print("\n")

if s == 'R':
    print(f"you choose regular size pizza which cost u: {size_regular}")

    if b == 'T':
        print(f"you choose thin base on ur pizza which cost u: {base_thin}")

    elif b == 'A':
        print(f"you choose medium base on ur pizza which cost u: {base_medium}")

    elif b == 'D':
        print(f"you choose thick base on ur pizza which cost u: {base_thick}")

    else:
        print("you have to choose ur base !!!!")

    if b == 'T' or b == 'A' or b == 'D' and ch == 'E':
            print(f"you choose extra cheese on ur pizza which cost u: {extra_cheese}")

    elif b == 'T' or b == 'A' or b == 'D' and ch == 'C':    
            print(f"you choose regular cheese on ur pizza which cost u: {regular_cheese}")

    else:
            print("it's ok if u don't want to add cheese")
        
elif s == 'M':
    print(f"you choose medium size pizza which cost u: {size_medium}")

    if b == 'T':
        print(f"you choose thin base on ur pizza which cost u: {base_thin}")

    elif b == 'A':
        print(f"you choose medium base on ur pizza which cost u: {base_medium}")

    elif b == 'D':
        print(f"you choose thick base on ur pizza which cost u: {base_thick}")

    else:
        print("you have to choose ur base !!!!")

    if b == 'T' or b == 'A' or b == 'D' and ch == 'E':
            print(f"you choose extra cheese on ur pizza which cost u: {extra_cheese}")

    elif b == 'T' or b == 'A' or b == 'D' and ch == 'C':    
            print(f"you choose regular cheese on ur pizza which cost u: {regular_cheese}")

    else:
            print("it's ok if u don't want to add cheese")

elif s == 'L':
    print(f"you choose large size pizza which cost u: {size_large}")

    if b == 'T':
        print(f"you choose thin base on ur pizza which cost u: {base_thin}")

    elif b == 'A':
        print(f"you choose medium base on ur pizza which cost u: {base_medium}")

    elif b == 'D':
        print(f"you choose thick base on ur pizza which cost u: {base_thick}")

    else:
        print("you have to choose ur base !!!!")

    if b == 'T' or b == 'A' or b == 'D' and ch == 'E':
            print(f"you choose extra cheese on ur pizza which cost u: {extra_cheese}")

    elif b == 'T' or b == 'A' or b == 'D' and ch == 'C':    
            print(f"you choose regular cheese on ur pizza which cost u: {regular_cheese}")

    else:
            print("it's ok if u don't want to add cheese")

else:
    print("Good day sir hope ur day going well")

if s == 'R' and b == 'T' and ch =='E':
    print("your bill is:",size_regular + base_thin + extra_cheese)
     
elif s == 'R' and b == 'A' and ch =='E':
    print("your bill is:",size_regular + base_medium + extra_cheese)
     
elif s == 'R' and b == 'D' and ch =='E':
    print("your bill is:",size_regular + base_thick + extra_cheese)

elif s == 'R' and b == 'T' and ch =='C':
    print("your bill is:",size_regular + base_thin + regular_cheese)

elif s == 'R' and b == 'A' and ch =='C':
    print("your bill is:",size_regular + base_medium + regular_cheese)

elif s == 'R' and b == 'D' and ch =='C':
    print("your bill is:",size_regular + base_thick + regular_cheese)

elif s == 'R' and b == 'T':
    print("your bill is:",size_regular + base_thin)

elif s == 'R' and b == 'A':
    print("your bill is:",size_regular + base_medium)

elif s == 'R' and b == 'D':
    print("your bill is:",size_regular + base_thick)

if s == 'M' and b == 'T' and ch =='E':
    print("your bill is:",size_medium + base_thin + extra_cheese)
     
elif s == 'M' and b == 'A' and ch =='E':
    print("your bill is:",size_medium + base_medium + extra_cheese)
     
elif s == 'M' and b == 'D' and ch =='E':
    print("your bill is:",size_medium + base_thick + extra_cheese)

elif s == 'M' and b == 'T' and ch =='C':
    print("your bill is:",size_medium + base_thin + regular_cheese)

elif s == 'M' and b == 'A' and ch =='C':
    print("your bill is:",size_medium + base_medium + regular_cheese)

elif s == 'M' and b == 'D' and ch =='C':
    print("your bill is:",size_medium + base_thick + regular_cheese)

elif s == 'M' and b == 'T':
    print("your bill is:",size_medium + base_thin)

elif s == 'M' and b == 'A':
    print("your bill is:",size_medium + base_medium)

elif s == 'M' and b == 'D':
    print("your bill is:",size_medium + base_thick)

if s == 'L' and b == 'T' and ch =='E':
    print("your bill is:",size_large + base_thin + extra_cheese)
     
elif s == 'L' and b == 'A' and ch =='E':
    print("your bill is:",size_large + base_medium + extra_cheese)
     
elif s == 'L' and b == 'D' and ch =='E':
    print("your bill is:",size_large + base_thick + extra_cheese)

elif s == 'L' and b == 'T' and ch =='C':
    print("your bill is:",size_large + base_thin + regular_cheese)

elif s == 'L' and b == 'A' and ch =='C':
    print("your bill is:",size_large + base_medium + regular_cheese)

elif s == 'L' and b == 'D' and ch =='C':
    print("your bill is:",size_large + base_thick + regular_cheese)

elif s == 'L' and b == 'T':
    print("your bill is:",size_large + base_thin)

elif s == 'L' and b == 'A':
    print("your bill is:",size_large + base_medium)

elif s == 'L' and b == 'D':
    print("your bill is:",size_large + base_thick)