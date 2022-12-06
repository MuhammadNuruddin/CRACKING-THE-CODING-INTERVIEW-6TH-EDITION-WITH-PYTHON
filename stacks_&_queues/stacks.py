"""
Impelement k stacks in single array in a time and space efficient way
"""
class Stacks:
    def __init__(self, k, n):
        self.k = k # number of stacks
        self.n = n # total size of array holding all the 'K' stacks

        # define array to holk the 'k' stacks
        self.arr = [0] * self.n

        # initiate all stacks with 0
        # ( -1 denotes stack is empty)
        self.top = [-1] * self.k

        # top of free stack
        self.free = 0

        # points to the next element in either 
        # 1. one of the 'k' stacks or 
        # 2. The 'free' stack
        self.next_node = [i + 1 for i in range(self.n)]  
        self.next_node[self.n - 1] = - 1

    # check whether given stack is empty
    def is_empty(self, stack):
        return self.top[stack] == -1

    # Check whether there is space left for the pushing new elements or not
    def is_full(self):
        return self.free == -1

    # Push item onto given stack number 
    def push(self, item, stack):
        if self.is_full():
            print('STACK OVERFLOW')
            return

        # Get 1st free slot to insert at
        insert_slot = self.free

        # Adjust free position
        self.free = self.next_node[self.free]

        # Insert the item at the free position we got above
        self.arr[insert_slot] = item    

        # Adjust next to point to to the old top of stack element
        self.next_node[insert_slot] = self.top[stack]  

        # Adjust next to point to the old top of stack element
        self.top[stack] = insert_slot

    # pop item from given stack number
    def pop(self, stack):
        if self.is_empty(stack):
            return None
        
        # get the item at the top of the stack
        top_element = self.top[stack]

        # Set new top of stack
        self.top[stack] = self.next_node[self.top[stack]]

        # push the old top element to free stack
        self.next_node[top_element] = self.free
        self.free = top_element

        return self.arr[top_element]
    
    def print_stack(self, stack):
        top_index = self.top[stack]
        while top_index != -1:
            print(self.arr[top_index])
            top_index = self.next_node[top_index]


if __name__ == '__main__':
    # create 3 stacks using array of size 10
    stacks = Stacks(3, 10)

    # push some items onto stack number 2
    stacks.push(15, 2)
    stacks.push(30, 2)

    # push some items onto stack 1
    stacks.push(29, 1)
    stacks.push(32, 1)
    stacks.push(45, 1)

    # push some items onto stack 0
    stacks.push(2, 0)
    stacks.push(10, 0)
    stacks.push(11, 0)

    stacks.print_stack(1)