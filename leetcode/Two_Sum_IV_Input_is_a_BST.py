# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        global mapped
        mapped = {}
        global ans
        ans = False

        def dfs(node):
          global ans
          global mapped
          if node is None:
            return
          remain = k - node.val
          if remain in mapped:
            ans = True  
            return
          if node.val not in mapped:
            mapped[node.val] = 1
          dfs(node.left)
          dfs(node.right)

        dfs(root)

        return ans