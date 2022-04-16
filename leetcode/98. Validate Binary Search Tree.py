# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.is_valid_bst(root, None, None)
        # return self.is_valid_bst2(root, -math.inf, math.inf)
    
    # first implement
    # Not only checking the parent's value,
    # but also you need to check all ancestors' value
    def is_valid_bst(self, root, left_boundary_exclusive, right_boundary_exclusive):
        if root is None:
            return True
        
        if left_boundary_exclusive is not None and root.val <= left_boundary_exclusive:
            return False
        
        if right_boundary_exclusive is not None and right_boundary_exclusive <= root.val:
            return False
        
        return self.is_valid_bst(root.left, left_boundary_exclusive, root.val) and self.is_valid_bst(root.right, root.val, right_boundary_exclusive)
    
    # better readability using math.inf
    def is_valid_bst2(self, root, left_boundary_exclusive, right_boundary_exclusive):
        if root is None:
            return True
    
        if root.val <= left_boundary_exclusive:
            return False
    
        if right_boundary_exclusive <= root.val:
            return False
    
        return self.is_valid_bst(root.left, left_boundary_exclusive, root.val) and self.is_valid_bst(root.right,
                                                                                                     root.val,
                                                                                                     right_boundary_exclusive)
print(Solution().isValidBST(TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)))) # true
print(Solution().isValidBST(TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None))))) # false
