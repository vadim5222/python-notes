def food_fill(image, sr, sc, new_color):
    old_color = image[sr][sc]
    if old_color == new_color:
        return image
    rows, cols = len[image], len(image[0])

    def dfs(r, c):
        if r < 0 or r > rows or c < 0 or c >= cols:
            return
        if image[r][c] != old_color:
            return
        image[r][c] = new_color
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)
    dfs(sr, sc)
    return image
image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, new=2