A = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
B = []
for string in A:
	print type(string)
	B += [list(string)]

def valid_box(a, b, board) :
    string = []
    padding_h = 3*a
    padding_v = 3*b
    array = 9*[0]
    for i in range(3):
        for j in range(3):
            k = board[padding_h + i][padding_v + j]
            if k != '.' :
                if array[int(k) - 1] == 0 :
                    array[int(k) - 1] = 1
                else :
                    return False
    return True

def valid_row(a, board) :
    string = []
    array = 9*[0]
    for i in range(9) :
        k = board[a][i]
        if k != '.':
            if array[int(k) - 1] == 0 :
                    array[int(k) - 1] = 1
            else :
                return False
    return True

def valid_column(a, board) :
    string = []
    array = 9*[0]
    for i in range(9) :
        k = board[i][a]
        if k != '.' :
            if array[int(k) - 1] == 0 :
                array[int(k) - 1] = 1
            else:
                return False
    return True

def sudoku_complete(board) :
    for string in board :
        if '.' in string :
            return False
    return True


def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    #print board
    if sudoku_complete(board) :
        return True
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                for k in '123456789' :
                    board[i] = board[i][:j] + k + board[i][j+1:]
                    if valid_box(i//3, j//3, board) and valid_row(i, board) and valid_column(j, board):
                        if solveSudoku(board) == True:
                        	return True
                    board[i] = board[i][:j] + '.' + board[i][j+1:]
                return False
    return False

print A
#B[0][0] = '9'
#print valid_row(0,B)
solveSudoku(A)
print A