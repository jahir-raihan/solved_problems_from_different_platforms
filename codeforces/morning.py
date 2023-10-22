t = int(input())
dig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for _ in range(t):
    inp = input()
    res = 0
    cursor = 1

    for i in inp:
        dis = abs(dig.index(int(i)) - cursor + 1) + 1
        cursor = dig.index(int(i)) + 1
        res += dis
    print(res)