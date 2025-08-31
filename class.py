# string slicing 

x = "22" 
y = "abcdefghijklmno" 
z = 22 + 2j
print(y[3:14:3])
print(y[-1])  #negative indexing strts from -1
# print(type(x)) 
# print(x[0])
# print(y[0])
# print(type(z)) 

p = int(input("enter your principal: "))
r = int(input("enter your rate: "))
t = int(input("enter your time: "))

i = (p*r*t)/100
print(f"the principal is {p} the rate is {r} the time is {t} and the interst is {i} ")
# print("entered amount is:", p, "ruppees rate is:", r, "percent time was:", t, "year simple interest is:", (p*r*t)/100)