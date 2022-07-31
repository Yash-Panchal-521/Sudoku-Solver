n=9

def isSafe(Sudoku,r,c,num):
    #checking row
    for i in range(9):
        if Sudoku[r][i]==num:
            return False
    
    #checking column
    for i in range(9):
        if Sudoku[i][c]==num:
            return False
        
    #cheking The box
    R=r-r%3
    C=c-c%3
    for i in range(3):
        for j in range(3):
            if Sudoku[R+i][C+j]==num:
                return False
    return True


def Solve(Sudoku,r,c):
    if r==n-1 and c==n:
        return True
    
    if c==n:
        r+=1
        c=0
    if Sudoku[r][c]>0:
        return Solve(Sudoku,r,c+1)
    
    for num in range(1,n+1):
        if isSafe(Sudoku,r,c,num):
            Sudoku[r][c]=num
            if Solve(Sudoku,r,c+1):
                return True
        Sudoku[r][c]=0
    return False

def Solver(Sudoku):
    if Solve(Sudoku,0,0):
        return Sudoku
    else:
        return "No"

