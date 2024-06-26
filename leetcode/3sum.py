class Solution:
    def threeSum(self, lst: List[int]) -> List[List[int]]:
        res = []
        lst.sort()
        for i, a in enumerate(lst):
            if i > 0 and a == lst[i - 1]:
                continue
            j, k = i + 1, len(lst) - 1

            while j < k:
                tmp = lst[i] + lst[j] + lst[k]
                if tmp > 0:
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    res.append([lst[i], lst[j], lst[k]])
                    j += 1
                    while lst[j] == lst[j - 1] and j < k:
                        j += 1
        return res
