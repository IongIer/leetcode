# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = []

        def dfs(root):
            if not root:
                return
            answer.append("(")
            answer.append(str(root.val))
            if not root.left and root.right:
                answer.append("()")
            dfs(root.left)
            dfs(root.right)
            answer.append(")")

        dfs(root)
        return "".join(answer)[1:-1]
