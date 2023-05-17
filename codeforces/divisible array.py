for _ in range(int(input())):
    n = int(input())

    arr = [i for i in range(1, n+1)]
    arr[0] += ((n*(n+1)) // 2) % n
    print(*arr)


