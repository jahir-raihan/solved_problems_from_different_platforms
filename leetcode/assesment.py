nums = [1, 2]
length = len(nums)
half_length = length // 2
nums.sort()

if half_length % 2 == 0:
    res = 0
    min_left = 0
    min_right = 0

    for i in range(1, half_length, 2):
        min_left += min(nums[i - 1], nums[i])
    for i in range(half_length + 1, length, 2):
        min_right += min(nums[i - 1], nums[i])
    print(min_left+min_right)
else:
    res = 0
    min_left = 0
    min_right = 0

    for i in range(1, half_length - 1, 2):
        min_left += min(nums[i - 1], nums[i])
    for i in range(half_length + 2, length, 2):
        min_right += min(nums[i - 1], nums[i])

    if length == 2:
        print(min(nums))

    min_left += min(nums[half_length - 1], nums[half_length+1])
    print(min_left + min_right)