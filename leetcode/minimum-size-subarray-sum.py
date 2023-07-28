target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
final_res = 999999999999

cur_count = 0
cur_sum = 0
i = 0
j = 0
while i < len(nums):

    if cur_sum >= target:
        final_res = min(cur_count, final_res)
        cur_sum -= nums[i]
        cur_count -= 1
        i += 1
    else:
        try:
            cur_count += 1
            cur_sum += nums[j]
            j += 1
        except:break
print(final_res if final_res != 999999999999 else 0)