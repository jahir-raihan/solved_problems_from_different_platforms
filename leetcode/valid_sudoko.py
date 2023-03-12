def check_row_column(board, r=True):
    v = {}
    for i in range(9):
        for j in range(9):
            tmp = board[i][j] if r else board[j][i]
            if tmp == '.':
                continue
            try:
                v[tmp] -= 1
                return False
            except:
                v[tmp] = 1
        v = {}
    return True


def check_cross(board):
    v = {}
    for i in range(3, 9 + 1, 3):
        cnt = 0
        for _ in range(3):
            for j in range(i - 3, i):
                for k in range(cnt, cnt + 3):

                    tmp = board[j][k]
                    if tmp == '.':
                        continue
                    try:
                        v[tmp] -= 1
                        return False
                    except:
                        v[tmp] = 1
            v = {}
            cnt += 3
    return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(check_row_column(board, r=False))
print(check_cross(board))


