# nums = [2, 3, 8, 4, 0, 0, 0, 0]
# res = True
# step = nums[0]
# arr = [step]
# for i in range(1, len(nums)-1):
#     step -= 1
#     if nums[i] == 0 and step == 0  and i != len(nums) - 1:
#         res = False
#         break
#     elif nums[i] > step:
#         step = nums[i]
#         arr.append(step)
#         continue
#     else:
#         arr.append(0)
# print(res)
#
# print(arr)



arr = [4,1,1,3,1,1,1]
jump = 0
init = arr[0]
i = 0
while i + init < len(arr) - 1:
    next_max = arr[i+1:i+init+1]
    next_idx = 0
    next_val = 0
    for idx, val in enumerate(next_max):
        if val+idx >= next_val + next_idx:
            next_val = val
            next_idx = idx


    init = next_val
    i = i + next_idx + 1
    jump += 1

if i != len(arr) - 1:
    jump += 1
print(jump)
