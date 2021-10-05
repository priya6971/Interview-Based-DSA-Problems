## Method Definition
def peakElement(arr):
    low = 0
    high = len(arr) - 1

    ## Base Case Conditions
    if len(arr) == 1:
        return 0
    if arr[0] > arr[1]: return 0
    if arr[-1] > arr[-2]: return len(arr) - 1
    ## Modified Binary Search Approach
    while low < high:
        mid = low + (high - low)//2
        if arr[mid] < arr[mid + 1]: 
            low = mid + 1
        else:
            high = mid 
    return low

## Driver Code
arr = [3, 5, 2, 4, 1]
arr1=[1]
result = peakElement(arr1)
print("Peak Element in a given array is:", result)
