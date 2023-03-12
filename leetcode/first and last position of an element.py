nums = [5,7,7,8,8,10]
target = 8
l, r = 0, len(nums) - 1
right = -1
while l <= r:
    mid = l + (r - l) // 2
    if nums[mid] == target:
        right = max(mid, right)
        l = mid + 1
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

left = 9999999999
l, r = 0, len(nums) - 1
while l <= r:
    mid = l + (r - l) // 2
    if nums[mid] == target:
        left = min(mid, left)
        r = mid - 1
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

print([left, right])