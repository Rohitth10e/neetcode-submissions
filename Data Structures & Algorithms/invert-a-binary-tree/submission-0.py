# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        res=[]

        if root is None:
            return None

        while q:
            currNode = q.popleft()
            currNode.left, currNode.right = currNode.right, currNode.left

            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return root