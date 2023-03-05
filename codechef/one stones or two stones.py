for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        if x % 2 == 0:
            print('CHEFINA')
        else:
            print('CHEF')
    elif abs(x - y) >= 2:
        if x > y:
            print('CHEF')
        else:
            print('CHEFINA')
    elif x % 2 == 1 and x > y:
        print('CHEFINA')
    elif (x % 2 == 0 and x > y) or (y % 2 == 0 and y > x):
        print('CHEF')
    else:
        print('CHEFINA')
