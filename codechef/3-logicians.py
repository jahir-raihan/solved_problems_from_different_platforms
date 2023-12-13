t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    no = False
    for i in s[:-1]:
        if i == '0' or no:
            print('NO')
            no = True
        else:
            print("IDK")
    if s[-1] == '1' and not no:
        print("YES")
    else:
        print("NO")
