# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = deque()
        q.append(root)
        seen = set()

        while q:
            curr = q.popleft()
            if curr not in seen:
                seen.add(curr)
                res.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        sroted = sorted(res)
        print(sroted)
        return sroted[k-1]
            