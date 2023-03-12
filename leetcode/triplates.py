nums = [4,4,2,4,3]
res = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] != nums[j] and nums[i]!=nums[k] and nums[j]!=nums[k]:
                res += 1

print(res)