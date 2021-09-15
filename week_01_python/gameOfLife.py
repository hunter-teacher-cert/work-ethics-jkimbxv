def createNewBoard(rows, cols):
    result = [[" " for c in range(cols)] for r in range(rows)];
    return result;

def printBoard(board):
    for r in board:
        for item in r:
            print(item+"|",end = '')
        print()

def setCell(board, r, c, val):
    board[r][c] = val;

def countNeighbors(board, r, c):
    numNeighbors = 0;
    startCol = c-1;
    endCol = c+1;
    startRow = r-1;
    endRow = r+1;
    #most top row
    if (r == 0 and c !=0 and c != len(board[0])-1):
        startRow = r;
    #most left col
    elif (c==0 and r!=0 and r!=len(board)-1):
        startCol = c;
    #most bottom row
    elif (r == len(board)-1 and c!= 0 and c!= len(board[0])-1):
        endRow = r;
    #most right cols
    elif (c==len(board[0])-1 and r!= 0 and r!=len(board)-1):
        endCol = c;
    else:
        startCol = c-1;
        endCol = c+1;
        startRow = r-1;
        endRow = r+1;
    #non edge cases
    for row in board[startRow:endRow+1]:
        for space in row[startCol:endCol+1]:
            if space=="X":
                numNeighbors+=1;
    return numNeighbors

def getNextGenCell(board,r,c):
    neigh = countNeighbors(board,r,c)
    if (neigh <2 or neigh >3):
      return ' ';
    elif (neigh == 3):
      return 'X';
    elif (neigh == 2):
      return board[r][c];
    else:
      return '-';

def generateNextBoard(board):
    nextBoard=createNewBoard(len(board),len(board[0]));
    r = 0;
    c = 0;
    while r<len(board):
        while c<len(board[0]):
            nextBoard[r][c] = getNextGenCell(board,r,c)
            c+=1
        r+=1;
    return nextBoard;

##function calls
newBoard = createNewBoard(4,4)
setCell(newBoard,1,1,'X')
setCell(newBoard,0,2,'X')
setCell(newBoard,0,3,'X')
printBoard(newBoard)
print("------------------")
printBoard(generateNextBoard(newBoard))
