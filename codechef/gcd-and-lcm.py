import math

t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())

    while k > 0 and x != y:
        if x > y:
            x = math.gcd(x, y)

            if x > y:
                x = math.lcm(x, y)
            else:
                y = math.lcm(x, y)
        else:
            y = math.gcd(x, y)

            if y > x:
                y = math.lcm(x, y)
            else:
                x = math.lcm(x, y)

        k -= 1
    print(x + y)