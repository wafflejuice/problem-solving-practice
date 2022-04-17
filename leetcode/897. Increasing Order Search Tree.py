# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.flatten(root)
        
    def flatten(self, root):
        if not root:
            return None

        new_root=root
        if root.left:
            new_root=self.flatten(root.left)
            
            new_parent=self.rightmost(new_root)
            new_parent.right=root
            root.left=None
        
        root.right=self.flatten(root.right)
        
        return new_root
    
    def rightmost(self, root):
        pre_root = root
        while root:
            pre_root = root
            root = root.right
        return pre_root

def printTree(root):
    from collections import deque
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        if not node:
            print('null', end=', ')
            continue
        
        print(node.val, end=', ')
        queue.append(node.left)
        queue.append(node.right)
    print()
    
s1=Solution().increasingBST(TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1,None,None),None),TreeNode(4,None,None)),TreeNode(6,None,TreeNode(8,TreeNode(7,None,None),TreeNode(9,None,None)))))
printTree(s1)
printTree(Solution().increasingBST(None))