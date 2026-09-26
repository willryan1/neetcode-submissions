# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def deep(node, curr):
            if node is None:
                return curr
            left = deep(node.left, curr + 1)
            right = deep(node.right, curr + 1)
            return max(left, right)
        
        return deep(root, 0)