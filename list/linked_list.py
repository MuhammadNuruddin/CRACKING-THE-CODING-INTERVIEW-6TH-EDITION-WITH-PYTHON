# Node Class - for each node
class Node:
    data = None
    next_node = None
    
    def __init__(self, data = None):
        self.data = data

    def __repr__(self):
        return '%s' %self.data

# Linked List Class - to join nodes
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        count_list = 0
        current = self.head
        while current:
            count_list += 1
            current = current.next_node
        return count_list
    
    def add(self, data):
        node = Node(data)
        node.next_node = self.head
        self.head = node
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def append_list(self, data):
        current = self.head
        node = Node(data)
        previous = None
        if self.is_empty():
            self.add(node)
        else:
            while current:
                previous = current
                current = current.next_node
            previous.next_node = node
        # return node
            
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            previous_node = current
            next_node = current.next_node

            previous_node.next_node = new
            new.next_node = next_node
        
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current #moves the pointer forward
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current 
    
    def __repr__(self):
        nodes = list()
        current = self.head
        while current:
        #     if current is self.head:
        #         nodes.append('[Head: %s]' %current.data) # uncomment to get styled repr
        #     elif current.next_node is None:
        #         nodes.append('[Tail: %s]' %current.data)
        #     else:
            nodes.append('%s' %current.data) # indent to get the styled repr
            current = current.next_node
        return ' --> '.join(nodes)
    


node_1 = Node(10)
node_2 = Node(3)
node_3 = Node(9)
node_1.next_node = node_3
node_3.next_node = node_2
linkedlist = LinkedList()
linkedlist.head = node_1
linkedlist.add(13)
linkedlist.add(34)
linkedlist.add(24)
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(4)
# linkedlist.insert(11,2)
linkedlist.append_list(22)

# print(linkedlist)