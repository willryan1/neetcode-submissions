# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.check(root, root.val)

    def check(self, node: TreeNode, msf: int) -> int:
        if not node:
            return 0
        count = 0
        if node.val >= msf:
            count += 1
        check_left = self.check(node.left, max(msf, node.val))
        check_right = self.check(node.right, max(msf, node.val))
        return count + check_left + check_right