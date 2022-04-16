from typing import *
from queue import PriorityQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val > other.node.val
    
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=PriorityQueue()
        self.generate_list(queue, root)
        
        pre_node=None
        while not queue.empty():
            node=queue.get()
            if pre_node:
                node.node.val+=pre_node.node.val
            pre_node=node
        
        return root
    
    def generate_list(self, queue, root):
        if not root:
            return
        
        queue.put(TreeNodeWrapper(root))
        self.generate_list(queue, root.left)
        self.generate_list(queue, root.right)
        