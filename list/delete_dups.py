"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

SOLUTION
In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table
will work well here.
In the below solution, we simply iterate through the linked list, adding each element to a hash table. When
we discover a duplicate element, we remove the element and continue iterating. We can do this all in one
pass since we are using a linked list.
"""

from linked_list import *
def delete_dup(node):
    new_set = set()
    previous = None
    while node != None:
        if node.data in new_set:
            previous.next_node = node.next_node
        else:
            new_set.add(node.data)
            previous = node
        node = node.next_node

    return new_set

# print(linkedlist)
# delete_dup(linkedlist.head)
# print(linkedlist)

# The above solution takes O(N) time, where N is the number of elements in the linked list.
"""
Follow Up: No Buffer Allowed
lf we don't have a buffer, we can iterate with two pointers: current which iterates through the linked list,
and runner which checks all subsequent nodes for duplicates.
"""

def delete_dups_no_buffer(node):
    current = node
    while current != None:
        # Remove all future nodes that have the same value
        runner = current
        while runner.next_node != None:
            if runner.next_node.data == current.data:
                runner.next_node = runner.next_node.next_node # set pointer to next to delete current
            else:
                runner = runner.next_node

        current = current.next_node

# This code runs in O ( 1) space, but O ( N2) time.   

print(linkedlist)
delete_dups_no_buffer(linkedlist.head)
print(linkedlist)