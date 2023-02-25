for _ in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    frq = [0] * (n + 1)
    for i in lst:
        frq[i] += 1
    frq.sort()
    if frq[-1] == frq[-2]:
        print(frq[-1])
    else:
        print(max(frq[-2], (frq[-1] // 2) + (frq[-1] % 2)))




