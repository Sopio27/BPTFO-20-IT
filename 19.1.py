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
    def append(self, value):

        #create new node
        new_node = Node(value) 

        #if linked list is empty, passed element becomes the head of the linked list 
        if self.head is None:
            self.head = new_node
            return

        
        #Code needs to get to the latest element of the list so we iterate
        #the list until we get to the latest node
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        #add data to the list
        current_node.next = new_node 

    #display values of the list
    def displayinfo(self):

        #print all values until we get to the latest element of the list
        current_node = self.head
        while current_node.next is not None:
            print(f"{current_node} ->")
            current_node=current_node.next

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

    #remove element from a given index
    def remove(self, index):
        #if index is zero, the second value becomes the head of the chain
        if index == 0:
            self.head = self.head.next
            return
        
        current_node = self.head
        node_index = 0
        
        #iterate the list until we reach the index before the index passed
        while current_node.next is not None and node_index < index - 1:
            node_index+=1
            current_node = current_node.next
       
        #removes the value from chain
        if current_node.next:
            current_node.next =current_node.next.next

#Stack
class Node:
   
    def __init__(self, data):
        #data of the node created
        self.data = data
        #data of the next node
        self.next = None 

class Stack:

    def __init__(self):
        #Top node of the stack. None if the stack is empty.
        self.top_node = None 
        #Length of stack is zero by default if no data is added
        self.length == 0 

    #check if stack is empty
    def isEmpty(self):
        return self.length == 0
    
    #return the length of the stack
    def size(self):
        return self.length
    
    #add new element to the stack
    def push(self, value):

        #create new node
        new_node = Node(value) 
        #if new element has been added, current top node becomes second in position
        new_node.next = self.top_node 
        #passed element becomes the top node
        self.top_node = new_node
        #length of the stack increases by one
        self.lenght += 1

    #get the top element of the stack
    def pop(self):

        #check if stack is not empty else return index error
        if not self.isEmpty:
            #get the top element of the stack
            popped_value = self.top_node.data
            #second value becomes new top node after retreiving data
            self.top_node = self.top_node.next 
            #length of stack decreases by 1
            self.length -= 1
            #return retreived element
            return popped_value
        
        else:

            raise IndexError