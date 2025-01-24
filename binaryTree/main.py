from binaryTree import BinaryTree

def main():
    tree = BinaryTree()
    print(hasattr(tree, 'create_binary_tree_alpha'))
    root_alpha = tree.create_binary_tree_alpha()
    root_num = tree.create_binary_tree_num()
    lst1 = tree.depth_first_list_rec(root_alpha)
    lst2 = tree.depth_first_list_dependent_rec(root_alpha)
    lst3 = tree.depth_first_traversal_list_iter(root_alpha)
    print(lst1)
    print(lst2)
    print(lst3)
    # tree.breadth_first_traversal(root_alpha)
    bfs_lst = tree.breadth_first_list(root_alpha)
    bfs_level_lst = tree.breadth_first_level_list(root_alpha)
    print(bfs_lst)
    print(bfs_level_lst)
    print(tree.sum_nodes_val(root_num))
    print(tree.max_node_val(root_num))
if __name__ == "__main__":
    main()
