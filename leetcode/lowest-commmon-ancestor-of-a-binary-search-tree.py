class Solution:
        
    def lca(self, root, n1, n2):

        # Base Case
        if root is None:
            return None

        # If both n1 and n2 are smaller than root, then LCA
        # lies in left
        if(root.val > n1.val and root.val > n2.val):
            return self.lca(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA
        # lies in right
        if(root.val < n1.val and root.val < n2.val):
            return self.lca(root.right, n1, n2)

        return root
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)
