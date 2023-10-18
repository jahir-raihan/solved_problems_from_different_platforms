t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = [int(i) for i in input().split()]

    sum_a = sum(a)
    dis = sum_a // n
    rem = sum_a % n

    if dis == 0 or (rem > 0 and k < 1):
        print("NO")
    else:
        print("YES")
