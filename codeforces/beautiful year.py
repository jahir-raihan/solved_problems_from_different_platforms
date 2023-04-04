n = f'{int(input())+1}'

while len(set(n)) != len(n):
    n = f'{int(n) + 1}'
print(n)