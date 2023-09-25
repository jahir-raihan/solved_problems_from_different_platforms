"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = [node]
        v = {}
        n_l = {}
        root = None
        n = None
        while q:
            tmp = q.pop()
            if tmp and tmp.val not in v:
                v[tmp.val] = 1
                if not root:
                    n = Node(1)
                    root = n
                    n_l[1] = n
                else:
                    n = n_l[tmp.val]
                lst = []
                for nb in tmp.neighbors:
                    if nb.val in n_l:
                        lst.append(n_l[nb.val])
                    else:
                        t = Node(nb.val)
                        n_l[nb.val] = t

                        lst.append(t)
                    q.append(nb)
                n.neighbors = lst
        return root
