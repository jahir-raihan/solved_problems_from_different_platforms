def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


t = int(input())

for _ in range(t):
    coordinates = []
    for i in range(4):
        i, j = map(int, input().split())
        coordinates.append((i, j))

    min_distance = 99999999999

    for i in range(4):
        for j in range(i+1, 4):
            min_distance = min(min_distance, distance(coordinates[i], coordinates[j]))
    print(int(min_distance**2))