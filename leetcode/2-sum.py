class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = defaultdict(list)
        l = len(nums)
        for i in range(l):
            dic[nums[i]].append(i)

        for i in range(l):
            try:
                tmp = (target) - (nums[i])
                val = dic[tmp]
                for j in val:
                    if j != i:
                        return [i, j]
            except:
                pass

# Updated

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, v in enumerate(nums):
            if target - v in dic:
                return [i, dic[target - v]]
            else:
                dic[v] = i

