from collections import Counter

t = int(input())

for _ in range(t):
    freq = Counter(input())
    perm = ''

    for i in range(int(input())):
        perm += input()

    res = 'YES'
    for i in perm:
        if i in freq and freq[i] > 0:
            freq[i] -= 1
        else:
            res = 'NO'
            break
    print(res)