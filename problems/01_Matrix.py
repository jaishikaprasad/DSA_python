# Leetcode Ques : 542 [01 Matrix]
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

def update_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # find the top and left
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                top = matrix[i-1][j] if i > 0 else float('inf')
                left = matrix[i][j-1] if j > 0 else float('inf')
                matrix[i][j] = min(top, left) + 1

    # find the bottom and right
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if matrix[i][j] != 0:
                down = matrix[i+1][j] if i < rows-1 else float('inf')
                right = matrix[i][j+1] if j < cols-1 else float('inf')
                matrix[i][j] = min(matrix[i][j], min(down, right)+1)

    return matrix
matrix = [[0,0,0],[0,1,0],[1,1,1]]
print(update_matrix(matrix))

# output : [[0, 0, 0], [0, 1, 0], [1, 2, 1]]