t = 1

for _ in range(t):
    n, m = 5, 2

    s = '10234'
    k = '57'

    moves = 99999999999999

    for i in range(n - m + 1):
        tmp = [int(j) for j in s[i:i + m]]

        tmp_moves = 0
        for j in range(m):
            tmp_moves += min(abs(tmp[j] - int(k[j])), 10 - (max(tmp[j], int(k[j]))) + min(tmp[j], int(k[j])))
        moves = min(tmp_moves, moves)
    print(moves)