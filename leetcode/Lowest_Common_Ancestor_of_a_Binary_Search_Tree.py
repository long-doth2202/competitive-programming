# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        while True:         
            if p.val <= root.val <= q.val:
                return root
            if p.val > root.val:
                root = root.right
            else:
                root = root.left