'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''


def data_validation(sudoku):
    list_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    for i in range(len(sudoku)):
        temp_list = list_num[:]
        #print("arey")
        for j in range(len(sudoku[0])):
            #print("jerey")
            if sudoku[i][j] in temp_list:
                temp_list.remove(sudoku[i][j])
                #print(temp_list)
        if len(temp_list) == 0:
            count += 1
            #print(count)
    if count != 9:
        return False  

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    #print(sudoku)
    global num_list
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    flag = data_validation(sudoku)
    if flag== True:
        for i in sudoku:
            for j in i:
                if j not in num_list:
                    return False
        return True
    return False
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
