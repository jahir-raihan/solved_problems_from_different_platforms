# This function returns next
# higher number with same
# number of set bits as x.
def snoob(x):
    next = 0
    if x:
        rightOne = x & -x
        nextHigherOneBit = x + int(rightOne)
        rightOnesPattern = x ^ int(nextHigherOneBit)
        rightOnesPattern = (int(rightOnesPattern) /
                            int(rightOne))

        rightOnesPattern = int(rightOnesPattern) >> 2

        next = nextHigherOneBit | rightOnesPattern
    return next



x = 23
print(snoob(x))

# This code is contributed by Smita
