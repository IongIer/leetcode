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
            if image[sr][sc] == initial:
                image[sr][sc] = color
                if 0 <= sr - 1 <= row and 0 <= sc <= col:
                    dfs(image, sr - 1, sc, initial, color)
                if 0 <= sr + 1 <= row and 0 <= sc <= col:
                    dfs(image, sr + 1, sc, initial, color)
                if 0 <= sr <= row and 0 <= sc - 1 <= col:
                    dfs(image, sr, sc - 1, initial, color)
                if 0 <= sr <= row and 0 <= sc + 1 <= col:
                    dfs(image, sr, sc + 1, initial, color)

        if initial != color:
            dfs(image, sr, sc, initial, color)
        return image
