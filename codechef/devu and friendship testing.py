# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = set(map(int, input().split()))
    cal = n - len(lst)
    print(n - cal)