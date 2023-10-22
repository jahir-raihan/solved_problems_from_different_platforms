from math import sqrt
t = int(input())


def dis(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


for _ in range(t):
    p = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    s = [0, 0]

    l1 = max(dis(s, a), dis(a, p))
    l2 = max(dis(s, b), dis(b, p))

    both = max(min(dis(s, a), dis(s, b)), min(dis(p, a), dis(p, b)), dis(a, b)/2)
    print(f'{min(l1, l2, both):.11f}')
