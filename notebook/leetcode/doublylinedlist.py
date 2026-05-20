class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
        head⬇️|⬇️tail
    None<-----[A]----> None
    
    
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 0
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev=new_node
            self.head = new_node
        self.length +=1
        return True
    def pop(self):

        """
                                    temp
         None --- [A] <---> [B] <---> [C] --- None
                head                    tail                  
        
        """
        if (self.length == 0):
            return
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    def pop_first(self):
        """
                 temp                     
         None --- [A] <---> [B] <---> [C] --- None
                head                    tail  
        """
        if (self.length == 0):
            return
        temp = self.head
        if (self.length ==1):
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp =self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
            return temp
    def set_value(self, index, value):
        temp = self.get(index, value)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index, value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True 
    
    def remove(self, index):
        if index < 0 or self.length <= index:
            return False
        if index==0:
            self.pop_first(index)
        if index == self.length:
            self.pop(index)
        temp = self.get(index-1)
        after = temp.next
        temp.next = after.next
        after.next = None
        after.prev = None
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()

        

                
        
    
        
    
        

        




    

    