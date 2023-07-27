words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

final_res = []
word_count = -1
char_count = 0


tmp_arr = []
i = 0
while i < len(words):

    condition = word_count + char_count + len(words[i]) > maxWidth

    if condition:
        exp = maxWidth - (word_count + char_count)
        space = exp // 2
        extra = exp % word_count if word_count > 0 else 0
        res = ''

        first_one = 1
        for w in tmp_arr:
            to_add = ''
            if exp - extra > 0:
                to_add += '#' * space
                exp -= space
            if word_count > 0 and first_one:
                to_add += '#' * extra
            elif word_count > 0:
                to_add += '#'
            res += w + to_add

            first_one = 0
            word_count -= 1
        final_res.append(res)
        tmp_arr = []
        word_count = -1
        char_count = 0

    else:
        word_count += 1
        char_count += len(words[i])
        tmp_arr.append(words[i])
        i += 1


res = ''
for w in tmp_arr:
    res += w + '#'
res = res + '#' * (maxWidth - len(res))
final_res.append(res)

print(final_res)


