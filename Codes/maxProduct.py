## Method Definition
## Data Structure : Heap
import heapq
def maxProduct(arr):
    a = heapq.nlargest(3, arr)
    b = heapq.nsmallest(2, arr)

    return max((a[2] * a[1] * a[0]), (b[1] * b[0] * a[0]))


## Driver Code
arr = [-2, -4, 5, 3]
arr1 = [1, 3, 4, 5]
result = maxProduct(arr)
result1 = maxProduct(arr1)
print("Maximum Product of three Numbers is", result)
print("Maximum Product of three Numbers is", result1)