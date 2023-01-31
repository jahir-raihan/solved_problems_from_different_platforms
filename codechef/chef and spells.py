for i in range(int(input())):
    lst = sorted(map(int, input().split()))
    print(lst[-1] + lst[-2])
