t = 1
for _ in range(t):
    a, b = 6, 4
    x = a ^ b
    t = bin(x)
    c = bin(x)[2:]
    y = pow(2,len(c)-1)
    print((2**len(c) - 1) ^ a)