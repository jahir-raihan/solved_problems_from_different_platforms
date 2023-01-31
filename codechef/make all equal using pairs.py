for _ in range(int(input())):
    n = int(input())
    dic = {}
    lst = list(map(int, input().split()))
    c_max = None
    for element in lst:
        try:
            dic[element] += 1
            if dic[element] > c_max:
                c_max = dic[element]

        except:
            dic[element] = 1
            if c_max is None:
                c_max = 1
    print(n - c_max)