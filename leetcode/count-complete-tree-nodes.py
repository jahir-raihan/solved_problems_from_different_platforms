class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l = root
        r = root
        h_l = 0
        h_r = 0
        while l:
            h_l += 1
            l = l.left
        while r:
            h_r += 1
            r = r.right
        if h_l == h_r:
            return pow(2, h_l) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)