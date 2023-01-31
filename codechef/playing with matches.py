# cook your dish here
dic = {
    0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6
}

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = a + b
    cnt = 0
    while c:
        cnt += dic[c % 10]
        c = c // 10
    print(cnt)
