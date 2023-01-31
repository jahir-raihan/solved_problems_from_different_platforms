for i in range(int(input())):
    n = int(input())
    if n*(n+1)//2 % 2 == 0:
        print(n)
    else:
        print(n - 1)
