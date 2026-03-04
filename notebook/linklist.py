class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
        
class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length =1
    def print_value(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def pop(self):
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -+1
            
        
my_linked_list = LinkedList(4)
my_linked_list.append(7)

my_linked_list.print_value()




# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)




                                                                                                                     