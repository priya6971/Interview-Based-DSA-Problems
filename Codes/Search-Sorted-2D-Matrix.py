## Searching of an element in 2D Matrix
## Given that integers in each row and column are sorted in an ascending order
## Approach : Modified Binary Search
## Method Definition
def searchMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1
    n = len(matrix)
    while(i < n and j >= 0):
        if matrix[i][j] == target:
            return True
        elif(matrix[i][j] > target):
            j -= 1
        else:
            i += 1
    
    return False

## Driver Code
matrix = [[1, 4, 7, 11, 15],[2, 5, 8, 12, 19],[3, 6, 9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
target = 5
res = searchMatrix(matrix, target)
print("Result is", res)