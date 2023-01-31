from math import log

for __ in range(int(input())):
    a, b = map(int, input().split())
    answer = 0
    while b % a != 0:
        a //= 2
        answer += 1

    answer += int(log(b // a, 2))
    print(answer)
