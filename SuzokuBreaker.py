from random import sample

base = 2
side = 2
size = 2
board = []


def setBase(newBase):
    global base, side,size
    if newBase > 4 or newBase < 2:
        print("Base must be 2, 3 or 4.")
        return
    base = newBase
    side = base * base
    size = side * side


def pattern(r, c):
    return (base*(r % base)+r//base+c) % side


def genBoardSol():
    global board
    rBase = range(base)
    rows = [g*base + r for g in sample(rBase, base)
            for r in sample(rBase, base)]
    cols = [g*base + r for g in sample(rBase, base)
            for r in sample(rBase, base)]
    nums = sample(range(1, side+1), side)
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

def genBoard():
    global board
    nRemove = size * 3//4
    for p in sample(range(size),nRemove):
        board[p//side][p%side] = 0

def solveBox(row,col,value):
    for i in range(side):
        if (board[row][i] == value) or (board[i][col] == value):
            return False
    startBaseRow = row - row % base
    startBaseCol = col -col % base
    for i in range(base):
        for j in range(base):
            if board[startBaseRow+i][startBaseCol+j] == value:
                return False
    return True 

def solveBoardRec(row,col):
    global board
    if col == side:
        row += 1
        col = 0
    if row == side:
        return True
    if board[row][col] > 0:
        return solveBoardRec(row, col + 1)
    for value in range(1, side+1): 
        if solveBox(row, col, value):
            board[row][col] = value
            if solveBoardRec(row, col + 1):
                return True
    board[row][col] = 0
    return False

setBase(3)
genBoardSol()
print("===============================")
for row in board:
    print(row)
print("===============================")
genBoard()
for row in board:
    print(row)
print("===============================")
if base == 4:
    print("DANGER: Base 4 may take too long to solve.")
    print("===============================")
solveBoardRec(0,0)
for row in board:
    print(row)
print("===============================")
