# We will remove the largest elements for every K iterations
def k_largest(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

arr = [4,2,9,7,5,6,7,1,3]
k = 4
print(k_largest(arr,k))

def k_largest1(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]