for i in range(int(input())):
    d,l,r = map(int,input().split())
    if l <= d and r >= d:
        print('Take second dose now')
    elif l > d:
        print('Too Early')
    else:
        print('Too Late')