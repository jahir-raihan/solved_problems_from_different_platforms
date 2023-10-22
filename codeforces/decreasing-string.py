t = int(input())

for _ in range(t):
    s = input()
    pos = int(input()) - 1
    a = []
    length = len(s)
    state = pos < length
    s += '$'
    for c in s:
        while not state and a and a[-1] > c:
            pos -= length
            length -= 1
            a.pop()
            if pos < length:
                state = True
        a.append(c)
    print(a[pos], end='')




