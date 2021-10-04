## Method Definition
## Data Structure : Heap
import heapq
def kSmallest(matrix, k):
    n = len(matrix)
    heap = []
    result = -1
    for i in range(n):
        for j in range(n):
            ## Adding the values of the matrix inside the Heap Data Structure
            heapq.heappush(heap, matrix[i][j])
    
    for i in range(k):
        result = heapq.heappop(heap)
    
    return result

## Method Definition
matrix = [[1, 4, 7],[3, 5, 9], [6, 8, 11]]
k = 4
result = kSmallest(matrix, k)
print("Kth-Smallest Element of the Matrix is:", result)