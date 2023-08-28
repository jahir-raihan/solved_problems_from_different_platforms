class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s_dic = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            try:
                tmp = dic[pattern[i]]
                if tmp != s[i]:
                    return False
            except:
                try:
                    tmp1 = s_dic[s[i]]
                    return False
                except:
                    dic[pattern[i]] = s[i]
                    s_dic[s[i]] = 0
        return True