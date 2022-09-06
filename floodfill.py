from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initial = image[sr][sc]
        row = len(image) - 1
        col = len(image[0]) - 1

        def dfs(image, sr, sc):
            nonlocal row, col, initial, color
            l, r, u, d = sr - 1, sr + 1, sc - 1, sc + 1
            image[sr][sc] = color
            if 0 <= l:
                if image[l][sc] == initial:
                    dfs(image, l, sc)
            if r <= row:
                if image[r][sc] == initial:
                    dfs(image, r, sc)
            if 0 <= u:
                if image[sr][u] == initial:
                    dfs(image, sr, u)
            if d <= col:
                if image[sr][d] == initial:
                    dfs(image, sr, d)

        if initial != color:
            dfs(image, sr, sc)
