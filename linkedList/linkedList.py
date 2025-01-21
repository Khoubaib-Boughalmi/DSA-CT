from typing import Optional
from node import Node

def display_list(head: Node) -> None:
    current = head
    while current:
        print(current.val)
        current = current.next

        # 1 -> 2 -> 3 -> 4 -> 5
        # h

def delete_node(head: Node, target: int) -> Node:
    if head.val == target:
        head = head.next
        return head

    prev    :Optional[Node]   = None
    current :Optional[Node]   = head
    while current:
        if current.val == target:
            prev.next = current.next
            break
        current = current.next
    return head

#   [1] -> [2] -> [3] -> [4] -> Node                                        

def find_middle_node(head: Node) -> Optional[int]:
    if not head:
        return None
    slow: Node = head
    fast: Optional[Node] = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val

    
def detect_cycle(head: Node) -> bool:
    if not head:
        return False
    fast: Optional[Node] = head
    slow: Optional[Node] = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False
    
def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1
    node4.next = node5


    # display_list(head)
    # head = delete_node(head, 1)
    # print("******************")
    # print(find_middle_node(head))
    print(detect_cycle(head))
if __name__ == "__main__":
    main()