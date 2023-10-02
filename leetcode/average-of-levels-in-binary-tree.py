class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return

        queue = [root]
        level = []

        res = [root.val]

        while queue and root:
            cur_sum = 0
            cur_cnt = 0
            for node in queue:
                cur_sum += node.val
                cur_cnt += 1
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if cur_cnt > 0:
                res.append(cur_sum / cur_cnt)
            queue, level = level, []
        return res[1:]