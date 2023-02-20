for _ in range(int(input())):
    n = int(input())
    reach = [0, 0]
    s = input()
    res = 'NO'
    for i in s:
        if reach == [1,1]:
            res = 'YES'
            break
        elif i == 'U':
            reach[0] += 1
        elif i == 'D':
            reach[0] -= 1
        elif i == 'L':
            reach[1] -= 1
        else:
            reach[1] += 1
    if reach == [1, 1]:
        print('YES')
    else:
        print(res)



