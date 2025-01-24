from binaryTree import BinaryTree, Node
from typing import Optional


def maximumDepthofBinaryTree(root: Optional[Node]) -> int:
    if not root:
        return 0
    
    left_subtree = maximumDepthofBinaryTree(root.left)
    right_subtree = maximumDepthofBinaryTree(root.right)

    return 1 + max(left_subtree, right_subtree)

def pathSum_one(root: Optional[Node], target: int):
    if not root:
        return False
    if not root.left and not root.right:
        return root.value == target
    target -= root.value
    return pathSum_one(root.left, target) or pathSum_one(root.right, target)

def pathSum_two(root: Optional[Node], target: int):
    def _pathSum_two(root: Optional[Node], current_sum: int):
        if not root:
            return False
        current_sum += root.value
        if not root.left and not root.right:
            return current_sum == target
        return _pathSum_two(root.left, current_sum) or _pathSum_two(root.right, current_sum) 
    return _pathSum_two(root, 0)
    
def main():
    binaryTree = BinaryTree()

    root = binaryTree.create_binary_tree_num()
    print(maximumDepthofBinaryTree(root))
    print(pathSum_one(root, 11))
    print(pathSum_two(root, 11))


if __name__ == "__main__":
    main()