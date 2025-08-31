name = [10 , 54 , 35 , 76 , 23 , 92 , 45]
print("LISTS\n")
# sort
print(name)
name.sort() #returns the output in ascending order 
name.sort(reverse=2) # returns the output in descending order 
print(name, "\n")

# add value at last
name.append(29)
print(name, "\n")

# reverse the list
name.reverse()
print(name, "\n")

# insert the value at index
name.insert(2 , 53)
print(name, "\n")

# return the value which is poped up
e = name.pop(3)
print(e, "\n")

# pop-up the value in list 
name.pop(3)
print(name, "\n")

# remove the set value 
name.remove(45)
print(name, "\n")

# tuple 
gc = (543 , 34543 ,54 , 324 , 54 , 3)
bc = (45 , 345 , 35 , 3 , 3 , 5)
a , b , c , d , e , f = bc
ac = (42 , (56 , 67 , 36) , 663)
ui = [765 , 43, 9765 , 254 , 2546]

print("TUPLE")
print(type(gc),"\n")
print(gc.count(54),"\n")
print(gc.index(324),"\n")

# repeat the tuple
new = gc * 3
print(new, "\n")

# add 2 tuple in one tuple
sussy = gc + bc 
print(sussy, "\n")

# check the value if located in tuple 
print(45 in gc)
print(45 in bc, "\n")

# length 
print(len(gc), "\n")

# unpacking 
print(a , b , c , d , e , f, "\n")

# nested: check index inside the bracket of tuple
print(ac[0])
print(ac[1][2], "\n")

# coverting list to tuple 
uc = tuple(ui)
print(uc, "\n")

# some casual methods 
print(min(gc))
print(max(gc))
print(sum(gc))
print(sorted(gc))