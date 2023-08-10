
"""Intuition was simple, thanks to kevinsogo, if the current value is grater then
    next value it means we need current value times to sort it. Hence, we pick up
    the maximum out of them"""

t = int(input())

for _ in range(t):
    input()
    a = [*map(int, input().split())]
    print(max((v for v, w in zip(a, a[1:]) if v > w), default=0))
