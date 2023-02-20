for _ in range(int(input())):
    a, b, p, q = map(int,input().split())
    res = False
    if p % a == 0 and q % b == 0:
        res = abs((p / a) - (q / b)) < 2
    elif q % a == 0 and p % b == 0:
        res1 = abs((q / a) - (p / b)) < 2
    print('YES' if res else 'NO')
    
    # At last i made a great mathematical assumption.
