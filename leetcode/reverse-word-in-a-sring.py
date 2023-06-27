class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for w in s.strip().split(' ')[::-1]:
           if w != '':
               res.append(w)

        return ' '.join(res)