for i in range(int(input())):
    n = int(input())
    print('LIGHT' if n < 3 else 'MODERATE' if n >=3 and n < 7 else 'HEAVY')