def Linear_Search(arr, target, index=0):

    if index >= len(arr):
        return -1
    
    if arr[index] == target:
        return index
    
    return Linear_Search(arr, target, index + 1)


numbers = [64, 25, 12, 22, 11, 90, 5]

print("Array:", numbers)
print()

test_targets = [22, 5, 64, 100]

for target in test_targets:
    result = Linear_Search(numbers, target)
    
    
    print(f"Searching for {target}:")
    print(f"index: {result}")
    
    if result != -1:
        print(f"Found at index {result}")
    else:
        print(f"Not found")
    print()