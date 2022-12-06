"""
Solution #2: Iterative Approach
We want to detect linked lists where the front half of the list is the reverse of the second half. How would we
do that? By reversing the front half of the list. A stack can accomplish this.
We need to push the first half of the elements onto a stack. We can do this in two different ways, depending
on whether or not we know the size of the linked list.
If we know the size of the linked list, we can iterate through the first half of the elements in a standard for
loop, pushing each element onto a stack. We must be careful, of course, to handle the case where the length
of the linked list is odd.
If we don't know the size of the linked list, we can iterate through the linked list, using the fast runner/ slow
runner technique described in the beginning of the chapter. At each step in the loop, we push the data from
the slow runner onto a stack. When the fast runner hits the end of the list, the slow runner will have reached
the middle of the linked list. By this point, the stack will have all the elements from the front of the linked
list, but in reverse order.
Now, we simply iterate through the rest of the linked list. At each iteration, we compare the node to the top
of the stack. If we complete the iteration without finding a difference, then the linked list is a palindrome.
"""
from linked_list import *
def iter_is_palindrome(head):
    # slow/fast runner technique
    slow = head
    fast = head

    stack = []
    """Push elements from first half of linked list onto stack. When fast runner
     (which is moving at 2x speed) reaches the end of the linked list, then we know we're at the middle"""

    while fast != None and fast.next_node != None:
        stack.append(slow.data)
        slow = slow.next_node
        fast = fast.next_node.next_node
    
    # Has odd number of elements, so skip the middle element
    if fast != None: slow = slow.next_node

    while slow != None:
        top = stack.pop()
        # If values are different, then it's not a palindrome
        if top != slow.data: return False
        slow = slow.next_node
    return True

linkedlist = LinkedList()
linkedlist.head = Node(0)
linkedlist.append_list(1)
linkedlist.append_list(2)
linkedlist.append_list(1)
linkedlist.append_list(0)
print(iter_is_palindrome(linkedlist.head))