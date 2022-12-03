"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order,such that the 1's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2.That is, 912.

SOLUTION
It's useful to remember in this problem how exactly addition works. Imagine the problem:
  6 1 7
+ 2 9 5
First, we add 7 and 5 to get 12. The digit 2 becomes the last digit of the number, and 1 gets carried over to
the next step. Second, we add 1, 1, and 9 to get 11. The 1 becomes the second digit,and the other 1 gets
carried over the final step. Third and finally, we add 1,6 and 2 to get 9. So,our value becomes 912.
We can mimic this process recursively by adding node by node,carrying over any "excess" data to the next
node. Let's walk through this for the below linked list:
    7 -> 1 -> 6
+   5 -> 9 -> 2

We do the following:
1. We add 7 and 5 first,getting a result of 12. 2 becomes the first node in our linked list,and we "carry" the
1 to the next sum.
List: 2 ->?
2. We then add 1 and 9, as well as the "carry;' getting a result of 11. 1 becomes the second element of our
linked list, and we carry the 1 to the next sum.
List: 2 -> 1 ->?
3. Finally, we add 6, 2 and our"carrY:'to get 9.This becomes the final element of our linked list.
List: 2 -> 1 -> 9.

"""
from linked_list import *
def sum_list(node_1, node_2,remainder = 0):
    if node_1 is None and node_2 is None and remainder == 0:
        return None
    result = Node()
    value = remainder
    if node_1 != None:
        value += node_1.data
    if node_2 != None:
        value += node_2.data
    result.data = value % 10 # Second digit of number
    # Recurse
    res = LinkedList()
    res.head = result
    m = Node()
    if node_1.next_node != None or node_2.next_node != None:
        m.data = sum_list(None if node_1 is None else node_1.next_node, None if node_2 is None else node_2.next_node, 1 if value >= 10 else 0)
        res.append_list(m)
    return res

node_1 = Node(6)
linkedlist1 = LinkedList()
linkedlist1.head = node_1
linkedlist1.add(1)
linkedlist1.add(7)

node_2 = Node(5)
linkedlist2 = LinkedList()
linkedlist2.head = node_2
linkedlist2.append_list(9)
linkedlist2.append_list(2)
print(sum_list(linkedlist1.head, linkedlist2.head))
# print(linkedlist1, linkedlist2)
