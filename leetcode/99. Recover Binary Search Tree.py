import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        visit=[]
        visit.append(TreeNode(-math.inf, None, None))
        self.inorder(root, visit)
        visit.append(TreeNode(math.inf, None, None))
        
        misplaces=[]
        for vi in range(1, len(visit)-1):
            if not (visit[vi-1].val < visit[vi].val < visit[vi+1].val):
                misplaces.append(visit[vi])
                
        t=misplaces[0].val
        misplaces[0].val=misplaces[-1].val
        misplaces[-1].val=t
        
    def inorder(self, root, visit):
        if root is not None:
            self.inorder(root.left, visit)
            visit.append(root)
            self.inorder(root.right, visit)
        
print(Solution().recoverTree(TreeNode(1, TreeNode(3, None, TreeNode(2, None, None)), None))) # [3,1,null,null,2]
print(Solution().recoverTree(TreeNode(3, TreeNode(1, None, None), TreeNode(4, TreeNode(2, None, None), None)))) # [2,1,4,null,null,3]
print(Solution().recoverTree(TreeNode(3, None, TreeNode(2, None, TreeNode(1, None, None))))) # [1,null,2,null,3]
print(Solution().recoverTree(TreeNode(1, TreeNode(3, None, TreeNode(2, None, None)))))
