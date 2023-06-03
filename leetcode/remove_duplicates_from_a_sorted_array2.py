nums = [0,0,1,1,1,1,2,3,3]

res = 0
cnt = 0
prev = None
for i in range(len(nums)):
    if nums[i] == prev and cnt > 1:
        nums[i] = 99999999
        res += 1
    elif nums[i] == prev:
        cnt += 1
        prev = nums[i]
    else:
        cnt = 1
        prev = nums[i]
nums.sort()
print(len(nums) - res)