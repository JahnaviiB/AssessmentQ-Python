def start(arr, target):
    if arr[0] == target:
        return 0
    l,r = 0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target and arr[mid-1]<target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
        return -1

def end(arr,target):
    if arr[-1] == target:
        return len(arr)-1
    l,r = 0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if  arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            r = mid-1
        else:
            l = mid +1
    return -1

def first_last(arr,target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    start = start(arr,target)
    end = end(arr,target)
    return[start,end]

arr = [ ]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = [input(), int(input())]
    arr.append(ele)

print(arr)
target = input("Enter the target ")
print(first_last(arr,target))




