from random import sample

base = -1
side = -1
size = -1
board = []


def setBase(newBase):
    global base, side,size
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


setBase(3)
genBoardSol()
for row in board:
    print(row)
print("===============================")
genBoard()
for row in board:
    print(row)
