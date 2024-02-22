class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

# [x]

class linkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        new_node = Node(value) # [x]

        if self.head is None:
            self.head = new_node
            return
        
        # როგორ ხდება მიჯაჭვა. უნდა გადაამოწმოს მონაცემის შემდეგი
        # ელემენტი თუ ცარიელია, მაშინ მანდ ჩაასკუპოს. მაგ ცარიელამდე უნდა
        # მივიდეს.

        #თავიდან ვაწყებინებთ
        current_node = self.head

        while current_node.next is not None: #ანალოგიური იქნებოდა: while current_node.next:
            current_node = current_node.next

        current_node.next = new_node 

    def displayinfo(self):

        current_node = self.head
        while current_node.next is not None:
            print(f"{current_node} ->")

    def insert(self, value, index):

        new_node = Node(value)

        if index == 0:
            indexzero = self.head #შეგეძლო თავში პირდაპირ მიგენიჭებინა:დ ესეც სწორია კიბატონო
            self.head = new_node
            new_node.next = indexzero
            return
        
        # 1[0] v 2[1] 3[2]

        current_node = self.head
        node_index = 0

        while current_node.next is not None and node_index < index - 1:
            current_node = current_node.next
            node_index+=1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        
        while current_node.next is not None and node_index < index - 1:
            current_node = current_node.next
            node_index+=1

        current_node.next =current_node.next.next
        