class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return print ('total nodes in linked list are' ,self.n)

    def insert_head(self,value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        self.n = self.n +1 

        
    def reverse_linked_list(self):
        prev_node = None
        current = self.head
        

        while current != None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        self.head = prev_node
        return print("After reversing the linked list :\n{}".format(l))      