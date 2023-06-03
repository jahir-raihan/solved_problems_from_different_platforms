nums = [2, 4, 1, 1, 0, 0]
res = True
step = nums[0]
arr = [step]
for i in range(1, len(nums)-1):
    step -= 1
    if nums[i] == 0 and step == 0  and i != len(nums) - 1:
        res = False
        break
    elif nums[i] > step:
        step = nums[i]
        arr.append(step)
        continue
    else:
        arr.append(0)
print(res)

print(arr)