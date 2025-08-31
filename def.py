# def sum(a,b):
#     c = a+b
#     print(f"The sum of {a} and {b} is: {c}")


# a = int(input("enter num a: "))
# b = int(input("enter num b: "))
# sum(a ,b)

# # c = int(input("enter num c: "))
# # d= int(input("enter num d: "))
# sum(int(input("enter num c: ")), "\n" , int(input("enter num c: ")))


# def leap_year(year):
#     if(year%4==0 )and(year%100 != 0)or(year%400==0):
#         print("Leap year")

#     else:
#         print("year isn't leap")

# leap_year(int(input("enter the year: ")))


# def leap_year(year , n):
#     month_1 = {"feb":28 , "odd": 31 , "even" : 30}
#     month_2 = {"feb":29 , "odd": 31 , "even" : 30}

#     if(year%4==0 )and(year%100 != 0)or(year%400==0):
#         print("Leap year")
#         if year == "Leap year" and n:
#             print()


#     else:
#         print("year isn't leap")

# leap_year(int(input("enter the year: ")))

# def check_prime(prime):
#     for i in range(2,prime):
#         if(prime%i==0):
#             print("Number is prime",prime)
#             break
#         else:
#             print("Number isn't prime")
#             break

# check_prime(11)


def name(f,l):
    if(f==" ")or(l==" "):
        print("You havenn't Enter Name")
    else:
        f_l=f+" " +l
        full=f_l.title()
        print(full)
    
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name(first_name , last_name)