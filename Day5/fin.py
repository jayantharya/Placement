"""#find
def greet(name):
    print("hello,",name)
greet("riya")
#logic
nums=[10,20,30]
for i in range(3):
    print(nums[i])
#bad
def f(x,y):
    z=x+y
    if z>100:
        print("yes")
    else:
        print("no")
f(65,86)
#good
def is_sum_above_limit(num1=59,num2=56,limit=100):
   #check if sum exceeds limit
    total=num1+num2
    if total>limit:
        print("sum exceeds limit")
    else:
        print("sum is within limit")
is_sum_above_limit(40, 65, 100)"""
#emp
"""from Git.Placement.Day_3.abstract import Vehicle
def linear_search(ids,target):
    for i in range(len(ids)):
        if ids[i]==target:
            return i
    return -1
ids=list(map(int,input().split()))
print(ids)
target=int(input())
print(linear_search(ids,target))
#def
def linear_search1(ids,target):
    for i in range(len(ids)):
        if ids[i]==target:
            return i
    return -1
ids=[101,205,310,415,520]
target=310
print(linear_search1(ids,target))"""

#binary
"""def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
num=list(map(int,input().split()))
num1=sorted(num)
#num=[1001,1002,1003,1004]
target=int(input())
result=binary_search(num1,target)
if result!=-1:
    print(f"ISBN NUMBER:",result)
else:
    print("not found")"""
#vech
"""def linear_search1(Vehicle,target):
    for i in range(len(Vehicle)):
        if Vehicle[i]==target:
            return i
    return -1
Vehicle=["KA05AB1234",
         "KA19SO3682",
         "KA11S0234"]
target="KA11S0234"
print(linear_search1(Vehicle,target))
print("vehicle found at slot",linear_search1(Vehicle,target))"""

#priorityqueue
"""from queue import PriorityQueue
hosp_queue=PriorityQueue()
hosp_queue.put((-2,"A(minor)"))
hosp_queue.put((-3,"B(medium)"))
hosp_queue.put((-1,"C(serious)"))
while not hosp_queue.empty():
    priority, name = hosp_queue.get()
    print(name)"""

#Binary
def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
num=[1005,1001,1020,1015,1010,1025]
print(num)
num1=sorted(num)
print(num1)
target=int(input())
result=binary_search(num1,target)
if result!=-1:
    print(f"product found at index: {result}")
else:
    print("product not found")