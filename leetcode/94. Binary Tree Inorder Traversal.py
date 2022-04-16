# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        traverse = []
        traverse += self.inorderTraversal(root.left)
        traverse += [root.val]
        traverse += self.inorderTraversal(root.right)
        
        return traverse

print(Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))))
print(Solution().inorderTraversal(None))
print(Solution().inorderTraversal(TreeNode(1, None, None)))