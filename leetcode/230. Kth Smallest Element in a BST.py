from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        self.inorder(l, root)
        
        return l[k-1].val
    
    def inorder(self, l, root):
        if not root:
            return
        
        self.inorder(l, root.left)
        l.append(root)
        self.inorder(l, root.right)
    
print(Solution().kthSmallest(TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4)), 1)) # 1
print(Solution().kthSmallest(TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1)),TreeNode(4)),TreeNode(6)), 3)) # 3