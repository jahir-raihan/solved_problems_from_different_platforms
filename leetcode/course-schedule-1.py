class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = collections.defaultdict(list)
        for k, v in prerequisites:
            adj_lst[k].append(v)

        vis = set()

        def dfs(crs):
            if crs in vis:
                return False
            if crs not in adj_lst:
                return True
            vis.add(crs)

            for v in adj_lst[crs]:
                if not dfs(v): return False
            vis.remove(crs)
            del adj_lst[crs]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True