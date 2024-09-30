class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        col_len = len(image[0])
        row_len = len(image)

        original_color = image[sr][sc]

        q = [(sr, sc)]
        vis = set()

        def get_adjecent(r, c):

            if r < row_len - 1 and image[r + 1][c] == original_color:
                q.append((r + 1, c))
            if r > 0 and image[r - 1][c] == original_color:
                q.append((r - 1, c))
            if c < col_len - 1 and image[r][c + 1] == original_color:
                q.append((r, c + 1))
            if c > 0 and image[r][c - 1] == original_color:
                q.append((r, c - 1))

        while q:
            current = q.pop(0)
            if current in vis:
                continue
            image[current[0]][current[1]] = color

            get_adjecent(*current)
            vis.add(current)

        return image
