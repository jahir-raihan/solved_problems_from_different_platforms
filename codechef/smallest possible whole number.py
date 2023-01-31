for i in range(int(input())):
    a,b = map(int, input().split())
    if b > 0:
        print(a%b)
    else:
        print(a)