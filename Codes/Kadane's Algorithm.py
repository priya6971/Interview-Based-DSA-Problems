## Algorithm Named : Kadane's Algorithm
## Time Complexity : O(n)
## Method Definition
def maxSubarray(arr):
    n = len(arr)
    max_sum = arr[0]
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    return max_sum
## Driver Code
arr = [-1, -3, 5, -4, 3, -6, 9, 2]
result = maxSubarray(arr)
print("Maximum Sum of a Subarray is:", result)