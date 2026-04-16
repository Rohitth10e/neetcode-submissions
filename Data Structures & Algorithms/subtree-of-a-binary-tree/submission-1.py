# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subtree_check(root, subRoot):
            if root is None and subRoot is None:
                return True
            
            if root is None or subRoot is None:
                return False
            
            return root.val == subRoot.val and subtree_check(root.left, subRoot.left) and subtree_check(root.right, subRoot.right)
        
        def find_subtree(root, subRoot):
            if root is None:
                return False
            
            return subtree_check(root, subRoot) or find_subtree(root.left, subRoot) or find_subtree(root.right, subRoot)
        
        return find_subtree(root, subRoot)