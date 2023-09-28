import math
t = int(input())

for _ in range(t):
    x = int(input())
    perc = (20/100)*x
    print(math.ceil(100 / perc))