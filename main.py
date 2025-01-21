from binaryTree import BinaryTree

def main():
    binaryTree = BinaryTree()
    root = binaryTree.create_binary_tree()
    lst1 = binaryTree.depth_first_list_rec(root)
    lst2 = binaryTree.depth_first_list_dependent_rec(root)
    lst3 = binaryTree.depth_first_traversal_list_iter(root)
    print(lst1)
    print(lst2)
    print(lst3)
    # binaryTree.breadth_first_traversal(root)
    bfs_lst = binaryTree.breadth_first_list(root)
    bfs_level_lst = binaryTree.breadth_first_level_list(root)
    print(bfs_lst)
    print(bfs_level_lst)

if __name__ == "__main__":
    main()
    [].so
