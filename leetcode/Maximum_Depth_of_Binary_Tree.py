# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        
        def dfs(root, depth):
            if (root is None):
                return
            global ans
            ans = max(ans, depth)
            if (root.left is not None):
                dfs(root.left, depth + 1)
            if (root.right is not None):
                dfs(root.right, depth + 1)

        dfs(root, 1)
        return ans