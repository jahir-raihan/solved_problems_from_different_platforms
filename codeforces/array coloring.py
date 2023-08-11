t = int(input())

for _ in range(t):
    input()
    a = [*map(int, input().split())]
    s = sum(a)
    print('Yes' if s % 2 == 0 else 'NO')