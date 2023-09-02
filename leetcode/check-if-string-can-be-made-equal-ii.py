from collections import Counter


def sol(s1, s2):
    return Counter(s1[i] for i in range(0, len(s1), 2)) == \
            Counter(s2[i] for i in range(0, len(s2), 2)) and \
            Counter(s1[i] for i in range(1, len(s1), 2)) == \
            Counter(s2[i] for i in range(1, len(s2), 2))


s = 'abcdba'
s1 = 'cabdab'

sol(s, s1)