
"""
Solution #3: Recursive Approach
First, a word on notation: in this solution, when we use the notation node Kx, the variable K indicates the
value of the node data, and x (which is either for b) indicates whether we are referring to the front node
with that value or the back node. For example, in the below linked list node 2b would refer to the second
(back) node with value 2.
Now, like many linked list problems, you can approach this problem recursively. We may have some intui­
tive idea that we want to compare element 0 and element n - 1, element 1 and element n - 2, element 2
and element n-3, and so on, until the middle element(s). For example:
0 ( 1 ( 2 ( 3 ) 2 ) 1 ) 0
In order to apply this approach, we first need to know when we've reached the middle element, as this will
form our base case. We can do this by passing in length - 2 for the length each time. When the length
equals 0 or 1, we're at the center of the linked list. This is because the length is reduced by 2 each time. Once
we've recursed N/2 times, length will be down to 0.

In the above call stack, each call wants to check if the list is a palindrome by comparing its head node with
the corresponding node from the back of the list. That is:
• Line 1 needs to compare node 0f with node 0b
• Line 2 needs to compare node 1 f with node lb
• Line 3 needs to compare node 2f with node 2b
• Line 4 needs to compare node 3f with node 3b.
If we rewind the stack, passing nodes back as described below, we can do just that:

Line 4 sees that it is the middle node (since length = 1), and passes back head. next. The value head
equals node 3, so head. next is node 2b.
Line 3 compares its head, node 2f, to returned_node (the value from the previous recursive call),
which is node 2b. lf the values match, it passes a reference to node lb (returned_node. next) up
to line 2.
Line 2 compares its head (node 1 f) to returned_node (node lb). If the values match, it passes a
reference to node 0b (or, returned_node. next) up to line 1.
Line 1 compares its head, node 0f, to returned_node, which is node 0b. If the values match, it
returns true.
To generalize, each call compares its head to returned_node, and then passes returned_node. next
up the stack. In this way, every node i gets compared to node n - i. If at any point the values do not
match, we return false, and every call up the stack checks for that value.
"""
from linked_list import *
class Result:
    node = None
    result = False
    
    def __init__(self, node, result):
        self.node = node
        self.result = result

def recur_is_palindrome(head):
    length  = length_of_list(head)
    p = is_palindrome_recurse(head, length)
    return p.result

def is_palindrome_recurse(head, length):
    if head != None and length <= 0: # even number of nodes
        return Result(head, True)
    elif length == 1: # odd number of nodes
        return Result(head.next_node, True)
    # Recurse on sublist.
    res = is_palindrome_recurse(head.next_node, length - 2)
    """ If child calls are not a palindrome, pass back up a failure. """
    if not res.result or res.node == None: return res
    # Check if matches corresponding node on other side.
    res.result = (head.data is res.node.data)
    # Return corresponding node.
    res.node = res.node.next_node
    return res

def length_of_list(head):
    size = 0
    while head != None:
        size += 1
        head = head.next_node
    return size

linkedlist = LinkedList()
linkedlist.head = Node(0)
linkedlist.append_list(1)
linkedlist.append_list(2)
linkedlist.append_list(1)
linkedlist.append_list(0)
print(recur_is_palindrome(linkedlist.head))