# cook your dish here
for _ in range(int(input())):
    input()
    n = input()
    if n == '1' or n == '10':
        print('NO')
    elif n.count('1') <= 3:
        print('YES')
    else:
        print('NO')




