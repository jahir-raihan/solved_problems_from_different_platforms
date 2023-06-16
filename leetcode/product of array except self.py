nums = [1,2,3,4]
n = len(nums)

# With O(n) and O(n)
# pre = [0]*n
# suf = [0]*n
#
# pre[0] = 1
# suf[n-1] = 1
#
# for i in range(1, n):
#     pre[i] = pre[i-1]*nums[i-1]
#
# for i in range(n-2, -1, -1):
#     suf[i] = suf[i+1] * nums[i+1]
#
# ans = [0]*n
#
# for i in range(n):
#     ans[i] = pre[i] * suf[i]
# print(pre, suf, ans)


# With O(n) and O(1)
ans = [1] * n

count = 1
for i in range(n):
    ans[i] *= count
    count *= nums[i]

count = 1
for i in range(n-1, -1, -1):
    ans[i] *= count
    count *= nums[i]
print(ans)