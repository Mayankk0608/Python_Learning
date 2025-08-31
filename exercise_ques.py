# ques 1 

a = int(input("Enter the first nunmber: "))
b = int(input("Enter the second number: "))

if a*b <= 1000:
    print(a*b)

else:
    print(a+b)

# ques 2 

for i in range(1 , 10):
    print(f"current number {i} previous number {i-1} sum: {i+i-1}")

# ques 3 

name = input("enter the name: ")
print(f"orignal name {name}")

after = list(name)
for i in after[0::2]:
    print(i)

# ques 4 

def list(number_list):
    print(f"given list: {number_list}")

    first_num = number_list[0]
    last_num = number_list[-1]

    if first_num == last_num:
        return True

    else:
        return False

list_1 = [34,45,76,987,34]
list_2 = [45,787,32,87,65]

print(f"result is: {list(list_1)}")
print(f"result is: {list(list_2)}")

# ques 5 

def greatest_num(a,b,c):
    if a > b and  a > c:
        return (f"the value {a} is greatest among all")
    
    elif b > a and b > c:
        return (f"the value {b} is greatest among all")

    elif c > a and  c > b:
        return (f"the value {c} is greatest among all")
    
a = int(input("enter the first value: "))
b = int(input("enter the second value: "))
c = int(input("enter the third value: "))

print(greatest_num(a,b,c))

# ques 6
    
def tempreture_convert_to_fahrenheit(n):
    return (9/5*n)+32 

celcius = int(input("celcius is: "))
print(f"Fahrenheit is: {tempreture_convert_to_fahrenheit(celcius)}")

# ques 7 

def tempreture_convert_to_celcius(n):
    return (5/9*(n-32))

Fahrenheit = int(input("Fahrenheit is: "))
print(f"{round(tempreture_convert_to_celcius(Fahrenheit),2)}\u00B0C")

# ques 8 

print("a")
print("b")
print("c", end='')
print("d")

# ques 9 

def sum(n):
    if n == 1:
        return 1
    
    else:
        return sum(n-1)+n
    
a = int(input("enter the number: "))
print(f"the sum of first {a} natural number is: {sum(a)}")

# ques 10 

def pattern(n):
    if n == 0:
        return 
    
    pattern(n-1)
    print("*"*n)

pattern_star = int(input("enter how many times u want to play the star pattern: "))
pattern(pattern_star)

# ques 11 

def inches_to_cm(n):
    return n*2.54

inches = int(input("inches is: "))
print(f"cm is: {inches_to_cm(inches)}")

# ques 12

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    
num = int(input("enter number for multiplication table: "))
multiplication_table(num)

# ques 13

def rem(l , word):
    n =[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 

list_1 = ["rihan", "ayaan", "sweta", "mayank"]
print(rem(list_1 , "an"))