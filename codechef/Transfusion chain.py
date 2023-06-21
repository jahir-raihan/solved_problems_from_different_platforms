t = int(input())

for _ in range(t):
    dic = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}
    n = int(input())
    donors = input().split()
    res = 0

    for i in donors:
        dic[i] += 1

    if dic['O'] > 0:
        res += dic['O']

    if dic['A'] > dic['B']:
        res += dic['A'] + dic['AB']
    elif dic['B'] > dic['A']:
        res += dic['B'] + dic['AB']
    elif dic['A'] == dic['B'] and dic['A'] > 0:
        res += dic['A'] + dic['AB']
    else:
        res += dic['AB']

    print(res)
