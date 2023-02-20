for _ in range(int(input())):
    n = int(input())

    s = input()
    count_i_distinct = 0
    count_j_distinct = 0
    vis_i, vis_j = {}, {}
    i, j = 0, n - 1
    while i <= j:
        if s[i] not in vis_i and s[j] not in vis_j:

            vis_i[s[i]] = 1
            vis_j[s[j]] = 1
            count_j_distinct += 1
            count_i_distinct += 1
            i += 1
            j -= 1
        elif s[j] not in vis_j:
            vis_j[s[j]] = 1
            count_j_distinct += 1
            j -= 1
        elif s[i] not in vis_i:
            vis_i[s[i]] = 1
            count_i_distinct += 1
            i += 1
        elif s[i] == s[j]:
            i += 1
            j -= 1
        else:
            count_j_distinct += 1
            j -= 1
            vis_j[s[j]] = 1
    print(count_j_distinct + count_i_distinct)