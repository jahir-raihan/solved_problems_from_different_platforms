# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    a_b = [i for i in range(a, b + 1)]
    c_d = [i for i in range(c, d + 1)]
    print(len(set(a_b + c_d)))
