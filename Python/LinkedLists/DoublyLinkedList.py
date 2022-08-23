
class Node(object):
    def __init__(self, value= None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList (object) :
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode


    def insertDLL(self, nodeValue , location):
        if self.head == None :
            print("The node cannot be inserted")
        else :
            newNode = Node(nodeValue)
            if location == 0 :
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1 :
                newNode.next = None
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail= newNode

            else :
                tempNode = self.head
                index = 0
                while index< location -1 :
                    tempNode = tempNode.next
                    index += 1
                if tempNode == self.head :
                    newNode.next = self.head
                    self.head.prev = newNode
                    self.head = newNode
                else :
                    newNode.next = tempNode.next
                    newNode.prev = tempNode
                    newNode.next.prev = newNode
                    tempNode.next = newNode

    def traversalDLL(self):
        if self.head is None :
            print("There is no element for traversal")
        else :
            node = self.head
            while node :
                print(node.value)
                node = node.next

    def traverseReverseDLL(self):
        if self.head is None:
            print("There is no element for traversal")
        else :
            node = self.tail
            while node :
                print(node.value)
                node = node.prev

    def searchDLL(self, value):
        if self.head == None :
            return "There is no element to search"
        else :
            tempNode= self.head
            while tempNode:
                if tempNode.value == value :
                    return tempNode.value
                tempNode = tempNode.next
            return (f"{value} is not present in the given linked list")

    def deleteDLL(self, location):

        if self.head is None :
            print("There is no element in DLL")
        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head = self.tail = None
                else :
                    self.head.next.prev = None
                    self.head = self.head.next

            elif location == -1 :
                if self.head == self.tail :
                    self.head = self.tail = None
                else :
                    self.tail = self.tail.prev
                    self.tail.next = None

            else :
                curNode = self.head
                index = 0
                while index< location-1 :
                    curNode  =curNode.next
                    index +=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has benn successfully deleted")

    def deleteEntireDLL(self):
        if self.head is None :
            print("There is no element in DLL")
        else :
            tempNode = self.head
            while tempNode :
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('The DLL is successfully deleted')

if __name__ == '__main__' :

    doublyLL = DoublyLinkedList()
    doublyLL.createDLL(5)

    doublyLL.insertDLL(0,1)
    doublyLL.insertDLL(9,0)
    doublyLL.insertDLL(34,-1)
    doublyLL.insertDLL(19,1)
    doublyLL.insertDLL(8,3)
    doublyLL.insertDLL(7,0)
    print([node.value for node in doublyLL])

    # doublyLL.traverseDLL()

    doublyLL.traverseReverseDLL()

    print(doublyLL.searchDLL(9))

    doublyLL.deleteDLL(-1)
    print([node.value for node in doublyLL])

    doublyLL.traverseReverseDLL()
    doublyLL.deleteEntireDLL()
    print([node.value for node in doublyLL])