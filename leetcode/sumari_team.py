
for i in range(int(input())):
    dic = {}
    nums = int(input())
    for j in range(nums):
        inp = input()
        dic[inp[0]] = dic[inp[0]] + 1 if inp[0] in dic else 1

    res = ''
    for k, v in dic.items():
        if v >= 3:
            res += k
    if res != '':
        print(''.join(sorted(res)))
    else:
        print('impossible')


