class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start_check = None
        idx = 0

        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0] and newInterval[1] >= intervals[i][0]:
                start_check = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                break
            idx += 1
            res.append(intervals[i])

        for i in range(idx, len(intervals)):

            if intervals[i][0] <= start_check[1]:
                start_check[1] = max(intervals[i][1], start_check[1])
            else:
                res.append(intervals[i])

        if start_check is None:
            res.append(newInterval)
        else:
            res.append(start_check)

        res.sort()

        return res