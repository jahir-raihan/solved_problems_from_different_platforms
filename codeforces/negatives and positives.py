for _ in range(int(input())):
    n = int(input())

    a = sorted(list(map(int, input().split())))
    count_of_neg = 0
    count_of_pos = 0

    neg_end = 0

    for i in range(n):
        if a[i] < 1:
            neg_end += 1
    i, j = 0, 1
    while j < neg_end:
        if a[i] <= a[j] and abs(a[i]) >= abs(a[j]):
            a[i] = a[i] * -1
            a[j] = a[j] * -1
        i += 1
        j += 1
    print(sum(a))




