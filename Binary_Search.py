def Binary_Search(arr, target, left=0, right=None):

    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return Binary_Search(arr, target, left, mid - 1)
    
    else:
        return Binary_Search(arr, target, mid + 1, right)

numbers = [64, 25, 12, 22, 11, 90, 5]

print("Original Array:", numbers)

numbers.sort()
print("Sorted Array:", numbers)
print()

test_targets = [22, 5, 64, 100]

for target in test_targets:
    result = Binary_Search(numbers, target)
    print(f"Searching for {target}:")
    print(f"index: {result}")
    
    if result != -1:
        print(f"Found at index {result}")
    else:
        print(f"Not found")
    print()