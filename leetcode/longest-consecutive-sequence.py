class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 0:
            return 0
        cnt = 0
        prev = None
        tmp_cnt = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                prev = None
                cnt = max(tmp_cnt, cnt)
                tmp_cnt = 0
            else:
                tmp_cnt += 1
        cnt = max(tmp_cnt, cnt) + 1
        return cnt