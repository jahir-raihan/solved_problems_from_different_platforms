lst = []
l, r = 0,sum(lst)
for i, a in enumerate(lst):
    r -= a
    if l == r:
        pass
        # return i
    l += a
# return -1
