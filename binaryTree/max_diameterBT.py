from typing import Optional
from binaryTree import Node

###### BAD APPROACH O(N^2) ######
class Solution:
    def max_tree_height(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return 1 + max(self.max_tree_height(root.left), self.max_tree_height(root.right))

    def _diameterOfBinaryTree(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        left_height = self.max_tree_height(root.left)
        right_height = self.max_tree_height(root.right)

        self.max_diameter = max(self.max_diameter, left_height + right_height)

        self._diameterOfBinaryTree(root.left)
        self._diameterOfBinaryTree(root.right)

        return self.max_diameter

    def diameterOfBinaryTree(self, root: Optional[Node]) -> int:
        self.max_diameter = 0
        self._diameterOfBinaryTree(root)
        return self.max_diameter
   
    
###### Good APPROACH O(N) ######
def diameterOfBinaryTree(self, root: Optional[Node]) -> int:
    max_diameter = 0
    def _diameterOfBinaryTree(root: Optional[Node]) -> int:
        nonlocal max_diameter 
        if not root:
            return 0
        left_height = _diameterOfBinaryTree(root.left)
        right_height = _diameterOfBinaryTree(root.right)

        max_diameter = max(max_diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
    _diameterOfBinaryTree(root)
    return max_diameter
