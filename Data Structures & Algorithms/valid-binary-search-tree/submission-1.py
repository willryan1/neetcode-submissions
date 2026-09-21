# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('-inf'), float('inf'))
    
    def check(self, root, v_min, v_max):
        if not root:
            return True
        if v_min >= root.val or v_max <= root.val:
            return False
        left = self.check(root.left, v_min, root.val)
        right = self.check(root.right, root.val, v_max)
        return left and right