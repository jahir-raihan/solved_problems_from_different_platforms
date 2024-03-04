for _ in range(int(input())):
    a, b, l = map(int,input().split())
    st = set()
    for i in range(21):
        for j in range(21):
            if l % (a ** i * b ** j) == 0:
                st.add(l//(a**i * b**j))
    print(len(st))
