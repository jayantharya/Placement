def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
arr=[10,25,37,42,58]
arr.insert(4,45)
print(arr)
arr.pop(1)
print(arr)
print(linear_search(arr,37))