import sys

#first constraint: row unique number
def row_check(row, num):

#second constraint: col unique number
def col_check(col, num):

#third constraint: 3x3 unique number (0-2, 3-5, 6-8)
def sub_check(row, col, num):

#ways to solve to first two constraint: loop to check before assignment (more processing time) / create array to store usage for checking (use more storage)

def boardExtract(file):
    board = [9][9]
    with open(file, 'r') as f:
        size = int(f.readline())
        delim = "[], \n"

def main(boardFile):
    board = boardExtract(boardFile)

if __name__ == '__main__':
    boardFile = sys.argv[1]
    main(boardFile)