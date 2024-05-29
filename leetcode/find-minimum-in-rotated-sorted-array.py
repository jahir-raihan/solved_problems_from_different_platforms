nums = [4,5,6,7,8, 90,1,2, 3]

n = len(nums)

min_val = nums[0]

if nums[0] > nums[-1]:
    l, r = 0, n - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] < nums[0]:
            min_val = nums[mid]
            r = mid - 1
        else:
            l = mid

print(min_val)