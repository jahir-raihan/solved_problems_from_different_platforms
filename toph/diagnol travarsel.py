import math

for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 1 and y == 1:
        print(f'Case {i + 1}: YES')

    else:
        res = math.sqrt(((1 - x) ** 2) + ((1 - y) ** 2))
        if res == int(res) and res > 0:
            print(f'Case {i + 1}: YES')
        else:
            print(f'Case {i + 1}: NO')
