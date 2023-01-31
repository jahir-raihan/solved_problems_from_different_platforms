# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    if n < 3:
        print(s)
    else:
        print(''.join(sorted(s)))