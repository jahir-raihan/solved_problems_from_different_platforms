for _ in range(int(input())):
    s = input()
    frq = {}
    for c in s:
        if c in frq:
            frq[c] += 1
        else:
            frq[c] = 1
    red = 0
    green = 0
    for k, v in frq.items():
        if v > 1:
            red += 1
            green += 1
        else:
            if green < red:
                green += 1
            else:
                red += 1
    print(red - 1 if red > green else red)
