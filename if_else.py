t_child = 500
c_child = 200
t_teen = 700
c_teen = 500
t_adult = 1000
c_adult = 700


h = int(input("Enter your height: "))
c = input('Enter "yes" is u want costume otherwise "no": ').upper()

# if h < 120:
#     print(f"ticket price for according {h}cm is {ticket_for_child}")

# elif h > 120 and h <180:
#     print(f"ticket price for according {h}cm is {ticket_for_teen}")
    
# else:
#     print(f"ticket price for according {h}cm is {ticket_for_adult}")
    

if h < 120:
    print(f"ticket price for according {h}cm is {t_child}")
    if c == "YES":
        print(f"costume price for according {h}cm is {c_child}")
        print("total cost" ,t_child + c_child)

elif h >120 and h <=180:
    print(f"ticket price for according {h}cm is {t_teen}")
    if c == "YES":
        print(f"costume price for according {h}cm is {c_teen}")
        print("total cost" ,t_teen + c_teen)

else:
    print(f"ticket price for according {h}cm is {t_adult}")
    if c == "YES":
        print(f"costume price for according {h}cm is {c_adult}")
        print("total cost" ,t_adult + c_adult)

