arr1=[20,4.90,10,5.0,3.096]
print("Traversal using for loop:")
for i in range(len(arr1)):
    print(f"Index{i}:{arr1[i]}")
arr2=arr1[4]
print(f"index{i}:{arr2}")
n=sorted(arr1)
print(n)
arr=['j',"jkd"]
print(arr)
#insertion
arr1.insert(2,30)
print("after insertion:",arr1)
#append
arr1.append(60)
print("after append:",arr1)
#deletion
arr1.remove(30)
print("after removing:",arr1)
popped=arr1.pop(2)
print(f"popped:{popped},array:{arr1}")