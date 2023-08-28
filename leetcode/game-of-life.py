board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]

change_state = {}


def count_neighbors(i, j, n, m):
    count = 0
    if i > 0 and board[i - 1][j] == 1:
        count += 1
    if i > 0 and j > 0 and board[i - 1][j - 1] == 1:
        count += 1
    if i > 0 and j < m and board[i - 1][j + 1] == 1:
        count += 1
    if i < n and board[i + 1][j] == 1:
        count += 1
    if i < n and j < m and board[i + 1][j + 1] == 1:
        count += 1
    if i < n and j > 0 and board[i + 1][j - 1] == 1:
        count += 1
    if j > 0 and board[i][j - 1] == 1:
        count += 1
    if j < m and board[i][j + 1] == 1:
        count += 1

    return count


n = len(board)
m = len(board[0])

for i in range(n):

    for j in range(m):
        con = count_neighbors(i, j, n - 1, m - 1)
        state = None
        if board[i][j] == 1:
            state = 0 if con < 2 or con > 3 else 1
        else:
            state = 0 if con < 3 or con > 3 else 1

        change_state[(i, j)] = state

for k, v in change_state.items():
    board[k[0]][k[1]] = v




