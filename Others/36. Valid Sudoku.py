'''
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

def isValidSudoku(board):
    from collections import Counter
    count = len(board)
    def checkRow(board):
        rowRes = True
        for i in range(count):
            temp = Counter(board[i])
            for key,val in temp.items():
                if not(key.isdigit()):
                    continue
                if not (int(key) <= 9 and int(val) == 1):
                    rowRes = False
            if rowRes == False:
                break
            else:
                continue
        return rowRes                     
    
    def checkCol(board):
        colRes = True
        temp = []
        for i in range(count):
            temp = []
            for j in range(len(board[i])):   
                element = board[j][i]
                if not element.isdigit():
                    continue
                temp.append(element)
            temp = Counter(temp)
            for key,val in temp.items():
                if not(key.isdigit()):
                    continue
                if not (int(key) <= 9 and int(val) == 1):
                    colRes = False
            if colRes == False:
                break
            else:
                continue      
        return colRes    
               
    def checkSubBox(board):
        for r in range(0, count, 3):
            for c in range(0, count, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True
    
    #checkRow(board)
    #checkCol(board)
    return checkRow(board) and checkCol(board) and checkSubBox(board)


Input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(Input))
        