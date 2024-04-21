from collections import defaultdict


class Solution:
    def dfs(self, adj_lst, node, vis, des):
        if node == des:
            return True

        vis[node] = 1
        for i in adj_lst[node]:
            if i not in vis and self.dfs(adj_lst, i, vis, des):
                return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst = defaultdict(list)

        for i, j in edges:
            adj_lst[i].append(j)
            adj_lst[j].append(i)

        return self.dfs(adj_lst, source, {}, destination)
