matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Find locations of the zeroes

locations = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            locations.append((i, j))


for loc in locations:

    for i in range(len(matrix[0])):
        matrix[loc[0]][i] = 0

    for i in range(len(matrix)):
        matrix[i][loc[1]] = 0
