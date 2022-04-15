from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        dummy_root=TreeNode(0, root, None)
        
        q=deque()
        q.append(dummy_root)
        while len(q)>0:
            curr=q.popleft()
            if not curr:
                continue
                
            if curr.left:
                if curr.left.val < low:
                    curr.left=curr.left.right
                    q.append(curr) # need to check the current node again
                # edge case: left value also can be higher than high limit
                elif high < curr.left.val:
                    curr.left=curr.left.left
                    q.append(curr) # need to check the current node again
                else:
                    q.append(curr.left)
            
            if curr.right:
                if high < curr.right.val:
                    curr.right=curr.right.left
                    q.append(curr) # need to check the current node again
                # edge case: right value also can be lower than low limit
                elif curr.right.val < low:
                    curr.right=curr.right.right
                    q.append(curr) # need to check the current node again
                else:
                    q.append(curr.right)
        
        return dummy_root.left
        
def printTree(root):
    from collections import deque
    
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        node=queue.popleft()
        if not node:
            print('null', end=', ')
            continue
            
        print(node.val, end=', ')
        queue.append(node.left)
        queue.append(node.right)
    print()

printTree(Solution().trimBST(TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2)) # [1,null,2]
printTree(Solution().trimBST(TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4)), 1, 3)) # [3,2,null,1]
printTree(Solution().trimBST(TreeNode(3), 2, 2)) # []
printTree(Solution().trimBST(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 3, 4)) # [3,null,4]