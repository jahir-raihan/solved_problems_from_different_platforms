def missingNumber(nums):
    ret = 0
    for i in range(len(nums)):
        ret ^= i
        ret ^= nums[i]

    ret ^= len(nums)
    return ret


missingNumber([0,1,3])
