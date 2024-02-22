#linked list
class Node:
    def __init__(self, data):
        #data of the node created
        self.data = data
        #data of the next node
        self.next = None


class linkedList:

    def __init__(self):
        #if linked list is empty, head is set to be none by default
        self.head = None

    #append new element to the list
    def append(self, data):

        #create new node
        new_node = Node(data) 

        #if linked list is empty, passed element becomes the head of the linked list 
        if self.head is None:
            self.head = new_node
            return

        
        #Code needs to get to the latest element of the list so we iterate
        #the list until we get to the latest node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        #add data to the list
        current_node.next = new_node 

    #display values of the list
    def displayinfo(self):

        #print all values until we get to the latest element of the list
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}")
            current_node = current_node.next
        

    #insert new element on a passed index
    def insert(self, value, index):
        
        #initialize new node
        new_node = Node(value)

        #check if index is zero, the value has to become the head of the chain.
        if index == 0:
            indexzero = self.head
            #new node becomes the head
            self.head = new_node
            #previous header becomes the second value of the chain
            new_node.next = indexzero
            return

        #if index is greater than zero, iterate through list until we get to the passed index and 
        #insert the element
        current_node = self.head
        node_index = 0

        #iterate until we get to the latest value or until we reach the index before the index passed
        while current_node.next is not None and node_index < index - 1:
            current_node = current_node.next
            node_index+=1

        #insert the data of the passed index into new node's next value
        new_node.next = current_node.next
        #new node becomes the next value of the chain
        current_node.next = new_node

    #remove a passed value
    def remove(self, value):

        if value == self.head.data:
           self.head = self.head.next
           return
          
        current_node = self.head
        node_index = 0

        while current_node.next and current_node.data == value:
            current_node = current_node.next
            node_index+=1
 
        if current_node.next:
            current_node.next =current_node.next.next

ll = linkedList()

ll.append(88)
ll.append(99)

ll.remove(88)
ll.displayinfo()
