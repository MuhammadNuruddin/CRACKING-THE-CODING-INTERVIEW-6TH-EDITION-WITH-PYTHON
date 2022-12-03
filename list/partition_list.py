"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

SOLUTION
If this were an array, we would need to be careful about how we shifted elements. Array shifts are very
expensive.
However, in a linked list, the situation is much easier. Rather than shifting and swapping elements, we can
actually create two different linked lists: one for elements less than x, and one for elements greater than or
equal to x.
We iterate through the linked list, inserting elements into our before list or our after list. Once we reach
the end of the linked list and have completed this splitting, we merge the two lists.
This approach is mostly "stable" in that elements stay in their original order, other than the necessary move­
ment around the partition. The code below implements this approach.
"""
from linked_list import *
def partition_list(node, x):
    before_start = None
    befrore_end = None
    after_start = None
    after_end = None

    # Partition the list
    while node != None:
        later_node = node.next_node
        node.next_node = None
        if node.data < x:
            # Insert node into end of before list
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next_node = node
                before_end = node
        else:
            # Insert node into end of after list
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next_node = node
                after_end = node
        
        node = later_node
    
    if before_start is None: return after_start
    # Merge before list and after list
    before_end.next_node = after_start
    return before_start


def partition(node, x):
    head, tail = node, node

    while node != None:
        later_node = node.next_node
        if node.data < x:
            # Insert node at head.
            node.next_node = head
            head = node
        else:
            # Insert node at tail.
            tail.next_node = node
            tail = node
        
        node = later_node

    tail.next_node = None

    return head

# print(linkedlist)
# print(partition_list(linkedlist.head, 10))
# print(linkedlist)
