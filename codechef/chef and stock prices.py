for i in range(int(input())):
    s,a,b,c = map(int, input().split())
    curr_price = s + c/100*s
    print('Yes' if a <= curr_price <= b else 'No')