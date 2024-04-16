# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def add(self, node, val, depth, cur_depth):

        if cur_depth == depth:
            new_node_left = TreeNode(val, left=node.left)
            new_node_right = TreeNode(val, right=node.right)

            node.left = new_node_left
            node.right = new_node_right
            return

        if node.left:
            self.add(node.left, val, depth, cur_depth + 1)
        if node.right:
            self.add(node.right, val, depth, cur_depth + 1)

        return

    def addOneRow(self, root, val: int, depth: int):

        if depth == 1:
            new_node = TreeNode(val, left=root)
            root = new_node
        self.add(root, val, depth - 1, 1)
        return root