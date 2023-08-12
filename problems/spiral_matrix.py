# Leetcode ques: 54 [spiral Matrix]
# Given an m x n matrix, return all elements of the matrix in spiral order.


def spiral_matrix(matrix):
    top_row = 0
    bottom_row = len(matrix)
    left_col = 0
    right_col = len(matrix[0])
    result = []

    while top_row < bottom_row and left_col < right_col:
        for i in range(left_col, right_col):
            result.append(matrix[top_row][i])

        top_row += 1
        for j in range(top_row, bottom_row):
            result.append(matrix[j][right_col-1])

        right_col -= 1
        if top_row < bottom_row:
            for i in range(right_col-1, left_col -1, -1):
                result.append(matrix[bottom_row-1][i])

            bottom_row -= 1

        if left_col < right_col:
            for j in range(bottom_row-1, top_row-1, -1):
                result.append(matrix[j][left_col])

            left_col += 1

    return result
matrix =  [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))

# Output = [1, 2, 3, 6, 9, 8, 7, 4, 5]