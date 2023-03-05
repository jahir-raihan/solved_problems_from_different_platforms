plus = 0
minus = 0
for _ in range(int(input())):
    s = input()
    if '+' in s:
        plus += 1
    else:
        minus += 1
print(plus - minus)