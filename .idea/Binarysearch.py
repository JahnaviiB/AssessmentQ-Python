def Binarysearch(array,x,low,high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high  = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 9
n = len(array)
result = Binarysearch(array,x,0,n-1)
print("Element is found at " + str(result))