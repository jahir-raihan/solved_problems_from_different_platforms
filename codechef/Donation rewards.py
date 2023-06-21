t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print('BRONZE')
    elif 3 < n <= 6:
        print('SILVER')
    else:
        print('GOLD')