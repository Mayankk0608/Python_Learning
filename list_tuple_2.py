# # ques1
# fruits = []

# f1 = input("fruit_1: ")
# fruits.append(f1)
# f2 = input("fruit_2: ")
# fruits.append(f2)
# f3 = input("fruit_3: ")
# fruits.append(f3)
# f4 = input("fruit_4: ")
# fruits.append(f4)
# f5 = input("fruit_5: ")
# fruits.append(f5)
# f6 = input("fruit_6: ")
# fruits.append(f6)
# f7 = input("fruit_7: ")
# fruits.append(f7)

# print(fruits, "\n")

# # ques2 
# marks = []

# s1 = int(input("marks_1: "))
# marks.append(s1)
# s2 = int(input("marks_2: "))
# marks.append(s2)
# s3 = int(input("marks_3: "))
# marks.append(s3)
# s4 = int(input("marks_4: "))
# marks.append(s4)
# s5 = int(input("marks_5: "))
# marks.append(s5)
# s6 = int(input("marks_6: "))
# marks.append(s6)

# print(marks)
# marks.sort()
# print(marks, "\n")

# # ques3
# a = (34 , 534 , "mayank")

# # a[1] = 43      #occures error 
# # print(a[1])

# # ques4
# mun = [34 , 43 , 76 , 13]       # using sum()
# sur = sum(mun)
# print(sur, "\n")

# sus = sum(mun ,45)    #using additional option
# print(sus, "\n")

# # ques5
# ggh = (7 , 0 , 8 , 0 , 0 , 9)
# print(ggh.count(0))





# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

n=int(input("Enter the number :"))
if(n%2!=0):
    print("Weird")
elif(n%2==0 and n >2 and n<5):
    print("not weird")
elif(n&2==0 and n >6 and n<20):
    print("Weird")
elif(n%2==0 and n>20):
    print("not weird")
