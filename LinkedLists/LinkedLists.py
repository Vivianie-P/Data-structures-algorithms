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



# Your MyLinkedList object will be instantiated and called as such:
myList = LinkedList()

node1 = Node(12)
node2 = Node(88)
node3 = Node(19)
node4 = Node(42)
node5 = Node(26)
node6 = Node(34)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

myList.head = node1

myList.print_list()
param_1 = myList.get(0)
print("\n")
print(param_1)

# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

    # def addAtHead(self, val: int) -> None:
    #     newHead = Node(val)

    # def addAtTail(self, val: int) -> None:

    # def addAtIndex(self, index: int, val: int) -> None:

    # def deleteAtIndex(self, index: int) -> None:
            

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
