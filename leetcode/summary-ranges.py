class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []
        if not nums:
            return []
        cur_str = f'{nums[0]}'
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if cnt > 0:
                    res.append(cur_str + '->' + f'{nums[i - 1]}')
                else:
                    res.append(cur_str)
                cur_str = f'{nums[i]}'
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            res.append(cur_str + '->' + f'{nums[-1]}')
        else:
            res.append(cur_str)
        return res
