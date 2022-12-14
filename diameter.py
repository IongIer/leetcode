from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr_best = 0

        def dfs(root):
            nonlocal curr_best
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            curr_best = max(curr_best, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return curr_best
