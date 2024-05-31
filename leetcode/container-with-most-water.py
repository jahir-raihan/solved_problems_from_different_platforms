class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        n = len(height)

        i, j = 0, n - 1
        while i < j:

            tmp = 0
            if height[i] < height[j]:
                tmp = height[i] * (j - i)
                i += 1
            elif height[i] > height[j]:
                tmp = height[j] * (j - i)
                j -= 1
            else:
                tmp = height[i] * (j - i)
                i += 1
            res = max(tmp, res)
        return res

