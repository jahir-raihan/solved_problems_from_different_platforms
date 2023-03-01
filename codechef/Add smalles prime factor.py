import math

for _ in range(int(input())):
    x, y = map(int, input().split())
    cnt = 0
    while x < y:
        num = x
        if num % 2 == 0:
            cnt += math.ceil((y-x)/2)
            break
        # iterate from 3 to sqrt(n)
        i = 3
        found = False
        while i * i <= x:
            if x % i == 0:
                x += i
                cnt += 1
                found = True
                break
            i += 2
        if not found:
            x += x
            cnt += 1
    print(cnt)

