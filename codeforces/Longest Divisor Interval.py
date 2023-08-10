t = int(input())
for i in range(t):

    # Starts checking from 1 and stops when a number is not divisible.
    # That's our interval

    n = int(input())
    j = 1
    while n % j == 0:
        j += 1
    print(j-1)
