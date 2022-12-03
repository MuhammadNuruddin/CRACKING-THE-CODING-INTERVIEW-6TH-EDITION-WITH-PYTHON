"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

SOLUTION
In this problem, you are not given access to the head of the linked list. You only have access to that node.
The solution is simply to copy the data from the next node over to the current node, and then to delete the
next node.
"""
from linked_list import *
def delete_middle_node(node):
    if node is None or node.next_node is None: return False
    node_after = node.next_node # next node
    node.data = node_after.data # copy data to current node
    node.next_node = node_after.next_node # set next node to 'node after' next node to delete 'node after
    return True

print(linkedlist)
print(delete_middle_node(node_3))
print(linkedlist)

"""
Note that this problem cannot be solved if the node to be deleted is the last node in the linked list. That's
okay-your interviewer wants you to point that out, and to discuss how to handle this case. You could, for
example, consider marking the node as dummy.
"""