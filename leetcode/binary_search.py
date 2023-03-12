nums = [22]
target = -6

l,r = 0, len(nums)-1

while l <= r:
    mid = (r + l) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1