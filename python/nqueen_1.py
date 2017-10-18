
def checkNQueen(row, column, current, N) :
    #print "row: ", row, "column: ", column, "N: ", N
    for i in range(N) :
        if current[row][i] == "Q" :
            return False
    for i in range(N) :
        if current[i][column] == "Q" :
            return False
    a = row
    b = column
    while a >= 0 and b >= 0 :
        # print "backward: ",a,b
        if current[a][b] == "Q" :
            return False
        a -= 1
        b -= 1

    a = row
    b = column
    while a >= 0 and b < N :
        # print "forward: ",a,b
        if current[a][b] == "Q" :
            return False
        a -= 1
        b += 1
    return True
def getNQueens(ans, row, current, N) :
    import copy
    if row >= N :
        temp = copy.deepcopy(current)
        ans.append(temp)
        # print hex(id(ans[-1]))
        # print current
        return
    for i in range(N) :
        if checkNQueen(row, i, current, N) :
            current[row] = current[row][:i] + 'Q' + current[row][i+1:]
            getNQueens(ans, row + 1, current, N)
            current[row] = current[row][:i] + '.' + current[row][i+1:]
    return
#class Solution(object):
#    def solveNQueens(self, n):
def solveNQueens(n):
    """
        :type n: int
        :rtype: List[List[str]]
        """
    output = []
    if n == 2 or n == 3 :
       return output
    current = n*[n*"."]
    getNQueens(output, 0, current, n)
    print output
    return output
solveNQueens(4)
solveNQueens(5)
