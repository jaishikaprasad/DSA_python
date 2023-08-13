# Leetcode Ques :59 [spiral Matrix II]
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

def spiral_matrixII(n):
    matrix = [[0]*n for i in range(n)]
    top_row = 0
    bottom_row = n
    left_col = 0
    right_col = n
    num = 1
    while top_row <= bottom_row and left_col <= right_col:
        for i in range(left_col, right_col):
            matrix[top_row][i] = num
            num += 1
        top_row += 1

        for j in range(top_row, bottom_row):
            matrix[j][right_col-1] = num
            num += 1
        right_col -= 1

        if top_row <= bottom_row:
            for i in range(right_col-1, left_col-1, -1):
                matrix[bottom_row-1][i] = num
                num += 1
            bottom_row -= 1
        
        if left_col <= right_col:
            for j in range(bottom_row-1, top_row-1 , -1):
                matrix[j][left_col] = num
                num += 1
            left_col += 1
    return matrix

print(spiral_matrixII(3))

# Output : [[1, 2, 3], [8, 9, 4], [7, 6, 5]]