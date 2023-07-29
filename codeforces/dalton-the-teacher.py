t = int(input())

for _ in range(t):
    n = int(input())

    arr = [int(i) for i in input().split()]
    res = 0
    counter = 0

    for i in range(n):
        if i + 1 == arr[i]:
            if counter > 0:
                counter -= 1
                res += 1
            else:
                counter += 1
    print(res + counter)