# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        def dfs(root, prev, curr):
            if not root:
                return
            prev += root.val
            curr.append(root.val)
            if prev == targetSum and not root.left and not root.right:
                answer.append(curr[:])
            dfs(root.left, prev, curr)
            dfs(root.right, prev, curr)
            curr.pop()

        dfs(root, 0, [])
        return answer
