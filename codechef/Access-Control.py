t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input()
    cur_swipe = 0
    for i in s:
        if i == '1':
            cur_swipe = x
        else:
            cur_swipe -= 1

        if cur_swipe < 0:
            break
    print("YES" if cur_swipe >= 0 else "NO")