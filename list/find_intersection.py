"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
-----
We should be careful here to not inadvertently draw a special case by making the linked lists the same
length.
Let's first ask how we would determine if two linked lists intersect.
Determining if there's an intersection.
How would we detect if two linked lists intersect? One approach would be to use a hash table and just
throw all the linked lists nodes into there. We would need to be careful to reference the linked lists by their
memory location, not by their value.
There's an easier way though. Observe that two intersecting linked lists will always have the same last node.
Therefore, we can just traverse to the end of each linked list and compare the last nodes.
How do we find where the intersection is, though?
Finding the intersecting node.
One thought is that we could traverse backwards through each linked list. When the linked lists"split'; that's
the intersection. Of course, you can't really traverse backwards through a singly linked list.
If the linked lists were the same length, you could just traverse through them at the same time. When they
collide, that's your intersection.
----
When they're not the same length, we'd like to just"chop off"-or ignore-those excess (gray) nodes.
How can we do this? Well, if we know the lengths of the two linked lists, then the difference between those
two linked lists will tell us how much to chop off.
We can get the lengths at the same time as we get the tails of the linked lists (which we used in the first step
to determine if there's an intersection).
Putting it all together.
We now have a multistep process.
1. Run through each linked list to get the lengths and the tails.
2. Compare the tails. If they are different (by reference, not by value), return immediately. There is no inter-
section.
3. Set two pointers to the start of each linked list.
4. On the longer linked list, advance its pointer by the difference in lengths.
5. Now, traverse on each linked list until the pointers are the same.
"""
from linked_list import *

class Result:
    tail = None
    size = 0
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def find_intersection(list_1, list_2):
    # Get tail and sizes.
    result_1 = get_tail_and_size(list_1)
    result_2 = get_tail_and_size(list_2) 

    # If different tail nodes, then there's no intersection.
    if result_1.tail !=  result_2.tail: return None
    # Set pointers to the start of each linked list.
    shorter = list_1 if result_1.size < result_2.size else list_2
    longer = list_2 if result_1.size < result_2.size else list_1
    # Advance the pointer for the longer linked list by difference in lengths.
    longer = get_kth_node(longer, abs(result_1.size - result_2.size))
    # Move both pointers until you have a collision.

    while shorter != longer:
        shorter = shorter.next_node
        longer = longer.next_node
    
    # Return either one.
    return longer

def get_tail_and_size(list):
    if list is None: return None
    size = 1
    current = list
    while current.next_node != None:
        size += 1
        current = current.next_node
    return Result(current, size)

def get_kth_node(head, k):
    current = head
    while k > 0 and current != None:
        current = current.next_node
        k -= 1
    return current

intersecting_node = Node(7)

head_1 = Node(3)
linkedlist1 = LinkedList()
linkedlist1.head = head_1
head_1.next_node = Node(1)
head_1.next_node.next_node = Node(5)
head_1.next_node.next_node.next_node = Node(9)
head_1.next_node.next_node.next_node.next_node = intersecting_node
head_1.next_node.next_node.next_node.next_node.next_node = Node(2)
head_1.next_node.next_node.next_node.next_node.next_node.next_node = Node(1)


head_2 = Node(4)
linkedlist2 = LinkedList()
linkedlist2.head = head_2
head_2.next_node = Node(6)
head_2.next_node.next_node = intersecting_node
head_2.next_node.next_node.next_node = Node(2)
head_2.next_node.next_node.next_node.next_node = Node(1)

print(linkedlist1, '<==>', linkedlist2)
print(find_intersection(linkedlist1.head, linkedlist2.head))