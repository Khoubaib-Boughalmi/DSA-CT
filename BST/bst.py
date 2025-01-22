from typing import Optional
from collections import deque
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

"""
    find the right place and return the new node to its parrent and assign it to the correct pointer
"""
def add_new_node_bst(root: Optional[Node], num: int) -> None:
    if root is None:
        return Node(num)
    
    if num > root.value:
        root.right = add_new_node_bst(root.right, num)
    elif num < root.value:
        root.left = add_new_node_bst(root.left, num)

    return root

def display_bst_level_by_level(root: Optional[Node]) -> None:
    result = []

    if root is None:
        print(result)
        return
    queue = deque([root])
    while queue:
        level = []
        level_len = len(queue)
        for _ in range(level_len):
            node = queue.popleft()
            level.append(node.value)
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
        result.append(level)

    print(result)

def main():
    nums = [6, 3, 8, 1, 5, 7, 9, 2]
    root = None
    root = add_new_node_bst(root, nums[0])
    for num in nums[1:]:
        root = add_new_node_bst(root, num)
    display_bst_level_by_level(root)

main()