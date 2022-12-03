"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

SOLUTION
We will approach this problem both recursively and non-recursively. Remember that recursive solutions are
often cleaner but less optimal. For example, in this problem, the recursive implementation is about half the
length of the iterative solution but also takes 0( n) space, where n is the number of elements in the linked
list.
Note that for this solution, we have defined k such that passing in k = 1 would return the last element,k = 2 would return to the second to last element, and so on. It is equally acceptable to definek such that k = 0 would return the last element.

Solution #1: If linked list size is known
If the size of the linked list is known, then thekth to last element is the ( length - k)th element. We can
just iterate through the linked list to find this element. Because this solution is so trivial, we can almost be
sure that this is not what the interviewer intended.

Solution #2: Recursive
This algorithm recurses through the linked list. When it hits the end, the method passes back a counter set
to 0. Each parent call adds 1 to this counter. When the counter equalsk, we know we have reached thekth
to last element of the linked list.
Implementing this is short and sweet-provided we have a way of"passing back" an integer value through
the stack. Unfortunately, we can't pass back a node and a counter using normal return statements. So how
do we handle this?
Approach A: Don't Return the Element.
One way to do this is to change the problem to simply printing thekth to last element. Then, we can pass
back the value of the counter simply through return values.
"""
from linked_list import *
def print_kth_to_last(node, k):
    if node is None: return 0
    index = print_kth_to_last(node.next_node, k) + 1

    if index == k:
        print(f'{index} "th to last element is" {node.data}')
    
    return index

# print_kth_to_last(linkedlist.head,3)

"""
Solution #3: Iterative
A more optimal, but less straightforward, solution is to implement this iteratively. We can use two pointers,
p1 and p2. We place them k nodes apart in the linked list by putting p2 at the beginning and moving p1
k nodes into the list. Then, when we move them at the same pace, p1 will hit the end of the linked list after
LENGTH - k steps. At that point, p2 will be LENGTH - k nodes into the list, or k nodes from the end.
"""

def kth_to_last(node, k):
    pointer_1 = node # p1
    pointer_2 = node # p2
    # Move p1 k nodes into the list.
    for i in range(k):
        if pointer_1 == None: return None # Out of bound
        pointer_1 = pointer_1.next_node

    # Move them at the same pace. When p1 hits the end, p2 will be at the right element.
    while pointer_1 != None:
        pointer_1 = pointer_1.next_node
        pointer_2 = pointer_2.next_node
    
    return pointer_2

print(kth_to_last(linkedlist.head,3))
# This algorithm takes O(n) time and 0(1) space.