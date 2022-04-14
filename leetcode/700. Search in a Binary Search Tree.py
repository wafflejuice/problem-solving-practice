from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBSTRecursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        
        return root
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while True:
            if root is None:
                return None
            
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root

def printTree(root):
    if root is None:
        print('None, ', end='')
    else:
        print(f'{root.val}, ', end='')
        printTree(root.left)
        printTree(root.right)

printTree(Solution().searchBST(TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, None, None)), 2)) # [2, 1, 3]
print()
printTree(Solution().searchBST(TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, None, None)), 5)) # []
print()