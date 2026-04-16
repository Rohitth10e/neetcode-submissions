# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def helper(node):
            nonlocal d
            if node is None:
                return 0
            
            d = max(d ,helper(node.left) + helper(node.right))

            return 1 + max(helper(node.left), helper(node.right))
        helper(root)
        return d
        