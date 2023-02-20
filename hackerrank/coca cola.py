for _ in range(int(input())):
    m, n, k = map(int, input().split())
    r = f'Case {_+1}: '
    print(r + 'Yes' if m // k >= n else r + 'No')