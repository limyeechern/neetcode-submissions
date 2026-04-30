# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        curr = root

        while curr:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                    continue
                curr.left = TreeNode(val)
                break
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                    continue
                curr.right = TreeNode(val)
                break
            
        return root
                
            