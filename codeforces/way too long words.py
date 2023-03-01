for _ in range(int(input())):
    s = input()
    if len(s) > 10:
        s = s[0] + f'{len(s[1:-1])}' + s[-1]
    print(s)