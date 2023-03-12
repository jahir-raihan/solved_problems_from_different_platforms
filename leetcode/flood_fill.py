image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2
t = image[sr][sc]
height = len(image)
width = len(image[0])
v = {}
q = [(sr, sc)]
if image[sr][sc] != color:
    while q:
        loc = q.pop()
        if f'{loc[0]},{loc[1]}' not in v:
            l, r = loc[0], loc[1]
            v[f'{l},{r}'] = 1
            image[l][r] = color
            if l < height-1 and image[l+1][r] == t:
                q.append((l+1, r))
            if l > 0 and image[l - 1][r] == t:
                q.append((l-1, r))
            if r < width - 1 and image[l][r + 1] == t:
                q.append((l, r+1))
            if r > 0 and image[l][r - 1] == t:
                q.append((l, r-1))


