t = int(input())
# I thought a lot about this approach, I hate my thought process speed.
# Understand the logic first then copy it, like i did.
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    for v in a[1:]:
        if v < b[-1]:
            b.append(1)
        b.append(v)

    print(len(b))
    print(*b)
