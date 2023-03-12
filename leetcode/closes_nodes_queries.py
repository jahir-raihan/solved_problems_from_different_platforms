class Solution:
    def closestNodes(self, root, queries):
        res = []
        for k in queries:
            mi = 0
            r1 = root
            while r1:
                if r1.val == k:
                    mi = r1.val
                    break
                if r1.val > k:
                    r1 = r1.left
                elif k > r1.val > mi:
                    mi = r1.val
                    r1 = r1.right
            mx = 9999999999
            r2 = root
            while r2:
                if r2.val == k:
                    mx = r2.val
                    break
                if k <= r2.val < mx:
                    mx = r2.val
                    r2 = r2.left
                elif r2.val < k:
                    r2 = r2.right
            res.append([mi if mi else -1, mx if mx != 9999999999 else -1])
        return res


# We have to reduce this algorithm time complexity.
