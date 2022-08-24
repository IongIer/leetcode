from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initial = image[sr][sc]
        row = len(image) - 1
        col = len(image[0]) - 1

        def dfs(image, sr, sc, initial, color):
            nonlocal row, col
            l, r, u, d = sr - 1, sr + 1, sc - 1, sc + 1
            if image[sr][sc] == initial:
                image[sr][sc] = color
                if 0 <= l <= row and 0 <= sc <= col:
                    if image[l][sc] == initial:
                        dfs(image, l, sc, initial, color)
                if 0 <= r <= row and 0 <= sc <= col:
                    if image[r][sc] == initial:
                        dfs(image, r, sc, initial, color)
                if 0 <= sr <= row and 0 <= u <= col:
                    if image[sr][u] == initial:
                        dfs(image, sr, u, initial, color)
                if 0 <= sr <= row and 0 <= d <= col:
                    if image[sr][d] == initial:
                        dfs(image, sr, d, initial, color)

        if initial != color:
            dfs(image, sr, sc, initial, color)
        return image
