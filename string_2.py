# ques1 
# a = input("Good Afternoon ")
name  = input("Enter ur name: ")
print(f"Good Afternoon {name}")

# ques2
print("")
b = input("Dear ")
print("You are selected")
c = input("Date: ")

# ques3
def has_double_space(text):
    return '  ' in text

d = "ore wa namaye wa hatake kakashi desu"
e = "ore wa namaye wa  hatake kakashi desu"
f = has_double_space(d)
g = has_double_space(e)
print("")
print(f)
print(g)

# ques4
h = e.replace("  ","   ")
print("")
print(h)

# ques5
i = "Dear! Mayank,\n\t\'One day u have to leave her\',\nthnx!"
print("")
print(i)