itr = 1


def count_n_say(num='1', itr=0):
    if itr == 0:
        return num
    new_str = ''
    repeat = num[0]
    curr_cnt_str = 0
    for i in num:
        if i == repeat:
            curr_cnt_str += 1
        else:
            new_str += str(curr_cnt_str) + repeat
            repeat = i
            curr_cnt_str = 1
    new_str += str(curr_cnt_str) + repeat
    itr -= 1
    return count_n_say(new_str, itr=itr)


print(count_n_say(itr=itr))
