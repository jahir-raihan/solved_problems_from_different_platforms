t = int(input())
vika = 'vika...'

for i in range(t):
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    counter = 0
    for j in range(m):
        for k in range(n):
            if s[k][j] == vika[counter]:
                counter += 1
                break
    print('Yes' if counter >= 4 else 'No')

# Understand the logic first then copy. I did the same.
