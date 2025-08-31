# The itertools module in Python provides a collection of fast, memory-efficient tools that allow for the creation of iterators for various tasks
import itertools


# Create a list (or any iterable)
# my_list = ["kick", "luck", "suck"]

# Use cycle to create an infinite loop
# for item in itertools.cycle(my_list):
    # print(item)

# basic use of for loop 
for i in itertools.count(10,2):
    print(i)
    if i >= 30:
        break


# infinte loop 
# super = ['A', 'B', 'C']
# for item in itertools.cycle(super):
    # print(item)


# Repeats an object indefinitely or a specified number of times
for hula in itertools.repeat('Hello', 5):
    print(hula)


# Combines multiple iterables into one long iterable
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for gay in itertools.chain(list1, list2):
    print(gay)


# Filters elements in data, returning only those elements for which the corresponding element in selectors is "True"/ "1"
data = 'ABCDEF'
selectors = [1, 0, 1, 0, 1, 0]
lesbian = list(itertools.compress(data, selectors))
print(lesbian)


# generates all possible co-ords according to length (permutations) of elements in the itertools
                        # any of the different ways in which a set of things can be ordered
baje = list(itertools.permutations('ABC', 2))
print(baje)


# generates all possible co-ords according to length combinations of elements in the itertools 
result = list(itertools.combinations('ABC', 2))
print(result)


# rerturns the product itertools with the elements value  
solve = list(itertools.product('AB', '12'))
print(solve)
print("")

# Groups consecutive elements in the iterable that have the same key value
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
grouped = itertools.groupby(data, key=lambda x: x[0])
for key, group in grouped:
    print(key, list(group))
print("")

# Slices an iterator, returning selected elements based on start, stop, and step
result_2 = list(itertools.islice(range(10), 2, 8, 2))
print(result_2)