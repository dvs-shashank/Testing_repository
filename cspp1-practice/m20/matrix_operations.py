def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    
    result_matrix = []
    for i in range(len(m1)):
        row_matrix = []
        for j in range(len(m2[0])):
            val = 0
            for k in range(len(m1[0])):
                val += m1[i][k] * m2[k][j]
            row_matrix.append(val)
        result_matrix.append(row_matrix)
    return result_matrix
    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result_matrix = []
    for i in range(len(m1)):
        row_matrix = []
        for j in range(len(m1[0])):
            row_matrix.append(m1[i][j] + m2[i][j])
        result_matrix.append(row_matrix)
    return result_matrix



def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    #ry:
    matrix_1 = read_matrix()
    # print(matrix_1)
    # read matrix 2
    matrix_2 = read_matrix()

    if matrix_1 != False and matrix_2 != False:
        # print(matrix_2)
        # add matrix 1 and matrix 2
        print(add_matrix(matrix_1, matrix_2))
        # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2))

def main():


    mat_1 = read_matrix()
    # read matrix 2
    mat_2 = read_matrix()
    # add matrix 1 and matrix 2
    print(add_matrix(mat_1, mat_2)) 
    # multiply matrix 1 and matrix 2
    print   (mult_matrix(mat_1, mat_2))
    

if __name__ == '__main__':
    main()
