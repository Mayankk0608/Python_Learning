data = {
    "kakashi": 100,
    "sweta": 75,
    "chotu": 50,
    "soahum": 25,
    "hushita": 85}

data.update({"kakashi": 150}) #for update the dict
data["chotu"] = 95    # also for update the dict

# prints the type of the variable
print(data, type(data))

# returns the value of key
print(data["hushita"])

# returns the keys and values of every elements 
print(data.items())

# returns only keys 
print(data.keys())

# returns the values of every key
print(data.values())

print(data)

# for adding extra element 
print(data.get("ivan"))

# for adding extra key & and its value
print(data.get("ivan", 450))
print(data)

# remove the key which user wants 
data.pop("soahum")
print(data, "\n")

# also for removing keys 
del data["chotu"]
print(data, "\n")

# for removing last key of dict 
data.popitem()
print(data, "\n")

# checking whether the key locates in dict or not
print("mayank" in data)
print("hushita" not in data)

# clear the dict  
print(data.clear())

# copy the dict to another variable 
datatype = data.copy()
print(data, "\n")
print(datatype)

# to set the common value in whole keys of a dict 
hulabuga = ["ab" , "bc" , "cd" , "da"]
chupa = dict.fromkeys(hulabuga, 45)
print(chupa)