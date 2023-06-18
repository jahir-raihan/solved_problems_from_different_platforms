t = int(input())

for _ in range(t):
    n = int(input())
    array = map(int, input().split())
    freq = [0]*100
    for i in array:
        freq[i] += 1

    res = 'Yes'
    for i in range(99, 0, -1):
        if freq[i-1] < freq[i]:
            res = 'No'
            break
    print(res)
