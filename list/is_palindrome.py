"""
Palindrome: Implement a function to check if a linked list is a palindrome.

SOLUTION
To approach this problem, we can picture a palindrome like 0 - > 1 - > 2 - > 1 - > 0. We know that,
since it's a palindrome, the list must be the same backwards and forwards. This leads us to our first solution.

Solution #1: Reverse and Compare
Our first solution is to reverse the linked list and compare the reversed list to the original list. If they're the
same, the lists are identical.
Note that when we compare the linked list to the reversed list, we only actually need to compare the first
half of the list. If the first half of the normal list matches the first half of the reversed list, then the second half
of the normal list must match the second half of the reversed list.
"""

from linked_list import *

def is_palindrome(head):
    reversed = reverse_and_clone(head)
    return is_equal(head, reversed)


def reverse_and_clone(node):
    head = None
    while node != None:
        cloned_node = Node(node.data) # clone node data
        cloned_node.next_node = head
        head = cloned_node
        node = node.next_node

    return head


def is_equal(node_1, node_2):
    while node_1 != None and node_2 != None:
        if node_1.data != node_2.data: return False
        node_1 = node_1.next_node
        node_2 = node_2.next_node
    return (node_1 is None and node_2 is None)

linkedlist = LinkedList()
linkedlist.head = Node(0)
linkedlist.append_list(1)
linkedlist.append_list(2)
linkedlist.append_list(1)
linkedlist.append_list(0)
print(is_palindrome(linkedlist.head))