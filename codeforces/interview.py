import sys
for _ in range(int(input())):
    x = int(input())
    a = list(map(int, input().split()))
    l, r = 0, x
    prev = None
    while l < r:
        mid = ((r-l+1)//2) + l
        mid_sum = 0
        if prev == f'{mid},{l}':
            print(mid)
            print('\n')
            sys.stdout.flush()
            break
        prev = f'{mid},{l}'
        for i in a[l:mid]:
            mid_sum += i

        q = f'? {mid}'
        for i in a[l:mid]:
            q += f' {i}'
        print(q)
        print('\n')
        sys.stdout.flush()
        s = int(input())
        if s > mid_sum:
            r = mid
        else:
            l = mid


