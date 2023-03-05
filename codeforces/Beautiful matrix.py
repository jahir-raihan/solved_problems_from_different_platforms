matrix = []
for _ in range(5):
    matrix.append(input().split())
loc_i = 0
loc_j = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            loc_i = i
            loc_j = j
            break

res = abs(2 - loc_i) + abs(2 - loc_j)
print(res)