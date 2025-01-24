from collections import deque
from typing import Optional

class Node:
    def __init__(self, value) -> None   :
        self.value: str= value
        self.left: "Node" | None = None
        self.right: "Node" | None = None

#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

'''
    The space complexity of a DFS depends on the height of the tree
    The space complexity of a BFS depends on the width of the tree
'''

class BinaryTree:
    def create_binary_tree_alpha(self) -> "Node":
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        return a

    def create_binary_tree_num(self) -> "Node":
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        f = Node(6)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        return a
        
    def depth_first_traversal_rec(self, root: "Node") -> None:
        if not root:
            return

        print(root.value)
        self.depth_first_list_rec(root.left)
        self.depth_first_list_rec(root.right)
    
    def depth_first_list_rec(self, root: "Node") -> list[str]:
        if not root:
            return []
        
        lst = [root.value]
        if root.left:
            lst.extend(self.depth_first_list_rec(root.left))
        if root.right:
            lst.extend(self.depth_first_list_rec(root.right))
        return lst
    
    def depth_first_list_dependent_rec(self, root: "Node") -> list[str]:
        if root is None:
            return []

        return self._depth_first_list_dependent_rec(root, [])

    def _depth_first_list_dependent_rec(self, root: "Node", result: list[str]) -> list[str]:
        result.append(root.value)
        if root.left:
            self._depth_first_list_dependent_rec(root.left, result)
        if root.right:
            self._depth_first_list_dependent_rec(root.right, result)
        return result


    def depth_first_traversal_list_iter(self, root: "Node") -> None:
        if not root:
            return

        result = []
        stack = list([root])
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

    def breadth_first_traversal(self, root: "Node") -> None:
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def breadth_first_list(self, root: "Node") -> list[str]:
        if not root:
            return

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
    def breadth_first_level_list(self, root: "Node") -> list[list[str]]:
        if root is None:
            return

        result = []
        queue = deque([root])
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def sum_nodes_val(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        
        return root.value + self.sum_nodes_val(root.left) + self.sum_nodes_val(root.right)
    
    def max_node_val(self, root: Optional[Node]) -> int:
        if not root:
            return float("-inf")
    
        max_left = self.max_node_val(root.left)
        max_right = self.max_node_val(root.right)

        return max(root.value, max_left, max_right)