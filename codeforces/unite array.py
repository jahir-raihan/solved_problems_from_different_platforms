for _ in range(int(input())):
    n = int(input())
    one = 0
    m_one = 0

    array = map(int, input().split())

    for i in array:
        if i == -1:
            m_one += 1
        else:
            one += 1

    diff = m_one - one
    if diff > 1:
        print(diff - one)
    elif diff == 0:
        print(0)
    elif diff < 0 and m_one % 2 != 0:
        pass
    else:
        print(1)