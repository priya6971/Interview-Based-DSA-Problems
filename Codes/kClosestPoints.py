## Method Definition
## Data Structure : Heap
import heapq
def kClosestPoint(points, k):
    n = len(points)
    def distance_points(x, y):
        return x ** 2 + y ** 2
    heap = []
    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heapq.heappush(heap, (distance_points(x,y), points[i]))
    
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
## Driver Code
points = [[2, -1],[3, 2],[4, 1],[-1, -1],[-2, 2]]
k = 3
res = kClosestPoint(points, k)
print("k Closest Points are:", res)