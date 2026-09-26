# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        
        def calc(node, level):
            if node is None:
                return
            if level not in d:
                d[level] = [node.val]
            else:
                d[level].append(node.val)
            left = calc(node.left, level + 1)
            right = calc(node.right, level + 1)
        
        calc(root, 0)
        sol = []

        i = 0
        while i in d:
            sol.append(max(d[i]))
            i += 1
        return sol