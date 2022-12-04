"""
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2.That is, 912.

Follow Up
Part B is conceptually the same (recurse, carry the excess), but has some additional complications when it
comes to implementation:
1. One list may be shorter than the other, and we cannot handle this "on the flY:' For example, suppose we
were adding (1 -> 2 -> 3-> 4) and (5-> 6-> 7). We need to know that the 5 should be"matched"with the
2, not the 1. We can accomplish this by comparing the lengths of the lists in the beginning and padding
the shorter list with zeros.
2. In the first part, successive results were added to the tail (i.e., passed forward). This meant that the recur­
sive call would be passed the carry, and would return the result (which is then appended to the tail). In
this case, however, results are added to the head (i.e., passed backward). The recursive call must return
the result, as before, as well as the carry. This is not terribly challenging to implement, but it is more
cumbersome. We can solve this issue by creating a wrapper class called Partial Sum.
"""

from linked_list import *
class PartialSum:
    sum = None
    remainder = 0

def add_list(node_1, node_2):
    len_1 = node_1.size()
    len_2 = node_2.size()
    # Pad the shorter list with zeros - see note (1)
    if len_1 < len_2:
        node_1 = padlist(node_1, len_2 - len_1)
    else:
        node_2 = padlist(node_2, len_1 - len_2)
    
    # Add lists
    sum = add_list_helper(node_1.head, node_2.head)
    # If there was a carry value left over, insert this at the front of the list. Otherwise, just return the linked list.
    if sum.remainder == 0:
        return sum.sum
    else:
        result = Node()
        result.data = insert_before(sum.sum, sum.remainder)
        return result
    

def add_list_helper(node_1, node_2):
    if node_1 is None and node_2 is None:
        sum = PartialSum()
        return sum
    
    # Add smaller digits recursively
    sum = add_list_helper(node_1.next_node, node_2.next_node)
    # Add carry to current data
    value = sum.remainder + node_1.data + node_2.data
    # Insert sum of current digits
    result = Node()
    result.data = insert_before(sum.sum, value % 10)
    # Return sum so far, and the carry value
    sum.sum = result
    sum.remainder = value//10
    return sum


# padd lists
def padlist(node, padding):
    head = node
    for i in range(padding):
        head = insert_before(head, 0)
    return head

# Helper function to insert node in the front of a linked list
def insert_before(list, data):
    node = Node(data)
    res = LinkedList()
    if list != None:
        node.next_node = list
    res.head = node
    return res

node_1 = Node(7)
linkedlist1 = LinkedList()
linkedlist1.head = node_1
linkedlist1.add(1)
linkedlist1.add(6)

node_2 = Node(2)
linkedlist2 = LinkedList()
linkedlist2.head = node_2
linkedlist2.append_list(9)
linkedlist2.append_list(5)
print(add_list(linkedlist1, linkedlist2))