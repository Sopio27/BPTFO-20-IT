class Node:
   
    def __init__(self, data):
        #data of the node given
        self.data = data #მიმდინარე მონაცემი
        #data of the next node
        self.next = None #მონაცემთან ერთად ინახება ინფორმაცია მომდევნო მონაცემის შესახებ


class Stack:

    def __init__(self):
        #Top node of the stack. None if the stack is empty.
        self.top_node = None # ინიცალიზაციისას ცარიელია საწყისი მონაცემი სანამ რამეს არ ჩავამატებთ და ზემოდან არ გადავაწერთ
        #Length of stack is zero by default if no data is added
        self.length == 0  #სტეკის სიგრძეც ნულია

    #check if stack is empty
    def isEmpty(self):
        return self.length == 0
    
    #return the length of the stack
    def size(self):
        return self.length
    
    #add new element to the stack
    def push(self, value):

        #create new node
        new_node = Node(value) #შეიქმნება ახალი კვანძი
        #if new element has been added, current top node becomes second in position
        new_node.next = self.top_node #სტეკის ქვედა მნიშვნელობა
        #passed element becomes the top node
        self.top_node = new_node #ზედა მნიშვნელობა გახდება ახალი
        #length of the stack increases by one
        self.lenght += 1 #სტეკის სიგრძე გაიზრდება 1-ით

    #get the top element of the stack
    def pop(self):

        #check if stack is not empty else return index error
        if not self.isEmpty:
            #get the top element of the stack
            popped_value = self.top_node.data
            #second value becomes new top node after retreiving data
            self.top_node = self.top_node.next #ქვედა ჩანაწერი გახდება უახლესი
            #length of stack decreases by 1
            self.length -= 1
            #return retreived element
            return popped_value
        
        else:

            raise IndexError