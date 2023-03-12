def count_one(n):
    cnt = 0
    while n:
        n = n&(n-1)
        cnt += 1
    return cnt



