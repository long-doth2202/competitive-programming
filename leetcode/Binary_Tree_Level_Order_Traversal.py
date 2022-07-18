# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ans = []

        while q:
            level = []
            for i in range(len(q)):
                v = q.popleft()
                if v:
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
            if (len(level)):
                ans.append(level)
        
        return ans
