stk = []
reverse = 0

while True:
    try:
        s = input().split()
        if s[0] == 'PUSH':
            val = int(s[1])
            if reverse:
                stk.insert(0, val)
            else:
                stk.append(val)

        elif s[0] == 'POP':
            if reverse:
                val = stk.pop(0)
            else:
                val = stk.pop()
        elif s[0] == 'PRINT':
            if len(stk) > 0:
                if reverse:
                    print(stk[0])
                else:
                    print(stk[-1])
            else:
                print('-')
        elif s[0] == 'SIZE':
            print(len(stk))
        elif s[0] == 'SUM':
            print(sum(stk))
        elif s[0] == 'REVERSE':
            reverse ^= 1

        elif s[0] == 'REPEAT':
            tmp = stk
            for r in range(int(s[1])):
                if len(stk) + len(tmp) <= 10**6:
                    stk = stk + [val for val in tmp]

    except:
        break


# Don't know why it is not working, i've tried my best, there's no other way ( in my opinion or thinking)
# to optimise it.
