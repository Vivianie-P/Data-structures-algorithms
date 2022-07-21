class Node: 
    def __init__(self, data):
        self.data = data #data of the node
        self.next = None #this is initalized next 


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        currNode = self.head
        while currNode is not None:
            print(str(currNode.data), end = " -> ")
            currNode = currNode.next

    def get(self, index: int) -> int:
        currIdx = 0
        currNode = self.head

        if index == 0:
            return currNode
        elif index < 0:
            return -1

        while currIdx < index:
            if currNode == None:
                return -1
            currNode = currNode.next
            currIdx += 1
        return currNode.data

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            currNode = self.head
            while (currNode.next):
                currNode = currNode.next
            currNode.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        currIdx = 0
        currNode = self.head

        if index == 0:
            self.addAtHead(val)
            return
        elif index < 0:
            print("ERROR: Invaild Index!")
            return

        while currIdx < index -1:
            if currNode is None:
                print("ERROR: Index is 3 more larger than the length of list!")
                return
            currNode = currNode.next
            currIdx += 1
        

        if currNode == None:
            print("ERROR: Index is larger than the length of list by 2!")
            return

        nodeAtIndex = currNode.next

        if nodeAtIndex is None:
            print("ERROR: Index is larger than the length of list by 1!")
            return
        
        if nodeAtIndex.next is None:
            self.addAtTail(val)

        newNode = Node(val)
        newNode.next = nodeAtIndex
        currNode.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        currIdx = 0
        currNode = self.head
        leadNode = self.head.next

        if currIdx == index:
            self.head = leadNode
            return
        
        while currIdx != index -1:
            if currNode is None:
                print("ERROR: Index is larger than the list")
                return

            currNode = currNode.next
            leadNode = leadNode.next
            currIdx += 1
            
        currNode.next = leadNode.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


myList = LinkedList()

node1 = Node(1)

myList.head = node1

myList.print_list()
print("\n\nAdding some more nodes:")
myList.addAtTail(2)
myList.addAtTail(3)
myList.addAtTail(4)
myList.addAtTail(5)
myList.print_list()

# print("\n\nAdding a Node at valid index (0):")
# myList.addAtIndex(0, 10)
# myList.print_list()

# print("\n\nAdding a Node at valid index (1):")
# myList.addAtIndex(1, 12)
# myList.print_list()

# print("\n\nIndex larger by 1!")
# myList.addAtIndex(7, 25)
# myList.print_list()

# print("\n\nIndex larger by 2!")
# myList.addAtIndex(8, 25)
# myList.print_list()

# print("\n\nIndex larger by 3!")
# myList.addAtIndex(9, 25)
# myList.print_list()

print("\n\n Deleting last index in list")
myList.deleteAtIndex(4)
myList.print_list()

print("\n\n Deleting first index in list")
myList.deleteAtIndex(0)
myList.print_list()

# list = LinkedList()
# print("\nInitial list: ")
# print(list.head)

# headNode = Node(45)
# list.head = headNode

# print("\nList after adding head node: ")
# print(list.head.data)

# new_node = Node(23)
# headNode.next = new_node
# print("\n")
# print(headNode.next.data)