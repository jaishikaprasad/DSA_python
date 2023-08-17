# Leetcode Ques : 48 [Rotate Image]
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

def rotate_image(matrix):
    l = len(matrix)

    # function to swap elements in place
    def swap(mat, i, j, x, y):
        mat[i][j], mat[x][y] = mat[x][y], mat[i][j]

    # Transpose of matrix
    for i in range(l):
        for j in range(i, l):
            swap(matrix, i, j, j, i)

    # Mirror half of the matrix
    for i in range(l):
        for j in range(l//2):
            swap(matrix, i, j, i, l-1-j)
    
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_image(matrix))

# output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]