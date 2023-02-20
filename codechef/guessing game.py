from math import gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd_val = gcd(a * b, a * b // 2)
    pairs = a * b // gcd_val
    can_choose = a * b // 2 // gcd_val
    if can_choose == 0:
        print('0/'+str(pairs))
    else:
        print(f'{can_choose}/{pairs}')
