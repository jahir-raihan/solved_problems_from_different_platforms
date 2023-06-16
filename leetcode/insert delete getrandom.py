nums = {1:0, 2:1, 3:1}
import random

lst = [k for k in nums.keys() if nums[k] > 0]
random_val = random.randint(0, len(lst) - 1)
print(lst[random_val])