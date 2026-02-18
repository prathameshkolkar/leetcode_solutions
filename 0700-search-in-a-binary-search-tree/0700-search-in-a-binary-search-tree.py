# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if root is None:
            return 
        curr=root
        while curr:
            if curr.val==k:
                return curr
            elif k>curr.val:
                curr=curr.right
            else:
                curr=curr.left
        return None
        