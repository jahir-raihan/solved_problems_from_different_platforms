class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = {}

        for c in ransomNote:
            try:
                ran[c] += 1
            except:
                ran[c] = 1

        mag = {}
        for c in magazine:
            try:
                mag[c] += 1
            except:
                mag[c] = 1

        res = True

        for k, v in ran.items():
            try:
                if mag[k] < v:
                    res = False
                    break
            except:
                res = False

        return res