import math

for i in range(int(input())):
    u, v, a, s = map(int, input().split())  # Taking input
    print('No' if ((u ** 2) - (
                2 * a * s)) > v ** 2 else 'Yes')  # as the law follows , if v^2 is grater then U^2 - 2as then yes else no


