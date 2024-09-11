s = "0A man, a plan, a canal: Panama"

c = ''
for i in s:
    if i.isnumeric() or i.isalpha():
        c += i.lower()

i, j = 0, len(c) - 1
while i < j:
    if c[i] != c[j]:
        res = False
        break

# New
class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = ''
        for i in s:
            if i.isalnum():
                new_str += i.lower() if i.isalpha() else i

        i, j = 0, len(new_str) - 1
        while i < j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1
        return True
