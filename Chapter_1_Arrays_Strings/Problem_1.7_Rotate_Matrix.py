import unittest
N = 4


def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix


# Function to pr the matrix
def displayMatrix(mat):
    for i in range(0, N):

        for j in range(0, N):
            print(mat[i][j], end=' ')
        print("")



    # Driver Code
mat = [[0 for x in range(N)] for y in range(N)]

# Test case 1
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

''' 
# Test case 2 
mat = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 

# Test case 3 
mat = [ [1, 2 ], 
        [4, 5 ] ] 

'''


# Print rotated matrix

rotate_matrix(mat)

displayMatrix(mat)

# This code is contributed by saloni1297
