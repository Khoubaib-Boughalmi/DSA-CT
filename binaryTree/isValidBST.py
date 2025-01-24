from typing import Optional
from binaryTree import Node

# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###### BAD APPROACH O(N^2) ######
class Solution:
    def binary_search(self, root: Optional[Node], target: int) -> bool:
        if not root:
            return False
        if root.val == target:
            return True
        if root.val < target:
            if self.binary_search(root.right, target):
                return True
        elif root.val > target:
            if self.binary_search(root.left, target):
                return True
        return False

    def isValidBST(self, root: Optional[Node]) -> bool:
        if not root:
            return True
        head = root
        visited = set()
        return self._isValidBST(root, root, visited)

    def _isValidBST(self, head: Node, root: Optional[Node], visited):
        if not root:
            return True
        if root.val in visited:
            return False
        visited.add(root.val)
        if not self.binary_search(head, root.val):
            return False
        return self._isValidBST(head, root.left, visited) and self._isValidBST(head, root.right, visited)

###### GOOD APPROACH time: O(N) space:O(N) ######

class Solution:
    def isValidBST(self, root: Optional[Node]) -> bool:
        if not root:
            return True
        visited = []
        def inorder_trav(root: Optional[Node], visited: set[int]) -> None:
            if not root:
                return True
            left = inorder_trav(root.left, visited)
            visited.append(root.val)
            right = inorder_trav(root.right, visited)

        inorder_trav(root, visited)
        for i in range(1, len(visited)):
            if visited[i-1] >= visited[i]:
                return False
        return True

