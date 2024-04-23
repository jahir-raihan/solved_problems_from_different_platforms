from collections import defaultdict


def dfs(node, adj_lst, depth, vis):
    cur_max = depth

    for i in adj_lst[node]:
        if i not in vis:
            vis.add(i)
            cur_max = max(cur_max, dfs(i, adj_lst, depth + 1, vis))
    return cur_max


def findMinHeightTrees(n, edges):
    min_nodes = []
    cur_min = 9999999999
    adj_lst = defaultdict(list)

    for i, j in edges:
        adj_lst[i].append(j)
        adj_lst[j].append(i)

    for i in range(n):
        s = set()
        s.add(i)
        val = dfs(i, adj_lst, 1, s)

        if cur_min == val:
            min_nodes.append(i)
        elif cur_min > val:
            cur_min = val
            min_nodes = [i]
    return min_nodes


result = findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
print(result)

# Top one is also valid, but it takes too much time to run

# Instead we'll use another approach called in-degree approach, where everytime leaf nodes
# Are deleted and new leaf nodes are determined after existing nodes from in-degrees


class Solution:

    def findMinHeightTrees(self, n, E):
        if not E: return [0]
        G, seen = defaultdict(set), [False] * n
        for u, v in E:
            G[u].add(v)
            G[v].add(u)
        leaves, new_leaves, in_degree = [], [], []
        for i in range(n):
            if len(G[i]) == 1:
                leaves.append(i)
            in_degree.append(len(G[i]))
        while n > 2:

            """
            for current leafs list, remove all of them and 
            reduce len of their connected parents, and determine if anyone of
            them becomes leafs and add that to leaves list again.
            """

            for leaf in leaves:
                for adj in G[leaf]:
                    in_degree[adj] -= 1
                    if in_degree[adj] == 1:
                        new_leaves.append(adj)
            n -= len(leaves)
            leaves = new_leaves[:]
            new_leaves.clear()

        return leaves