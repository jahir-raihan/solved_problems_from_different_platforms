dividend = -2147483648
divisor = -1

sign = 0 if ( (dividend < 0) ^ (divisor < 0)) else 1

d = abs(dividend)
ds = abs(divisor)
q = 0

while d >= ds:
    d -= ds
    q += 1
    print(q)
