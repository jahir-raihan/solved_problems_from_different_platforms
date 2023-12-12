orda = ord('a')
for _ in range(int(input())):
    n = int(input())

    frq = [0] * 26
    for c in input():
        frq[ord(c) - orda] += 1
    mx = max(frq)
    print(max(n % 2, 2*mx - n))
