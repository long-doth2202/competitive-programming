# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root, min_val, max_val):
            if root == None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return validBST(root.left, min_val, root.val) and validBST(root.right, root.val, max_val)

        max_val = (1 << 32) - 1
        min_val = -ma
        return validBST(root, min_val, max_val)