nums = [1, 1, 0, 1]
res = True
step = nums[0]
for i in range(1, len(nums)):
    step -= 1
    if nums[i] == 0 and step == 0  and i != len(nums) - 1:
        res = False
        break
    elif nums[i] > step:
        step = nums[i]
        continue

print(res)

