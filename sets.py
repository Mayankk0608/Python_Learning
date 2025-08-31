s = set() #for empty set      not repeatiton is allowed in sets 
d = {} #for empty dictionary 
# for user input 

s.add(input())
s.add(input())
s.add(input())
s.add(input())
s.add(input())  
s.add(input())
s.add(input())

print(s)

kilo = { 34 ,4 ,56, 98 , 87, 23}

# for removing the elements 
kilo.remove(34)
kilo.discard(23)
print(kilo, "\n")

# since set is an unaranged pop()method remove any random elements 
my_set = kilo.pop()
print(my_set)

# for joining the both sets 
mili = {76 , 87 , 90 , 98 }
print(mili, "\n")
milo  = kilo.union(mili)
print(milo)

# prints the elements which is common in both sets 
milo = kilo.intersection(mili)
print(milo, "\n")

# Returns a new set with elements in the first set that are not in the second set
milo = kilo.difference(mili)
print(milo)

# returns a new set which with elements with either side , not in both side 
milo = kilo.symmetric_difference(mili)
print(milo)

# for checking which set is superset or subset 
#   SUBSET = CHILD SET
#   SUPERSET = PARENT SET 
kili = {4 , 56 ,98}
print(kili.issubset(kilo))
print(kilo.issuperset(kili))

# used for checking whether that element located in set or not 
print(56 in kilo)
print(87 in mili)
print(67 in mili)

# update the set 
kilo.update({7 , 8 , 9})
print(kilo)

# prints the element which is common in set 
kilo.intersection_update({7 , 87 , 65})
print(kilo)

# remove the specific element which user wants 
kilo.difference_update({56})
print(kilo)

# remove the elements which is common in both side 
kilo.symmetric_difference_update(mili)
print(kilo) 