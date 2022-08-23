

class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList(object) :
    def __init__ (self) :
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next
            if node == self.tail.next :
                break

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node

    def insertCSLL(self, value , location):
        if self.head == None :
            return "The head reference is None"
        else :
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                self.tail.next = newNode
                self.head = newNode
            elif location == -1 :
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else :
                tempNode = self.head
                index = 0
                while index < location-1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseCSLL(self):
        if self.head is None :
            print("There is no element for traversal")
        else :
            tempNode = self.head
            while tempNode :
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next :
                    break

    def searchCSLL(self, nodeValue):
        if self.head is None :
            return "There is no element for traversal"
        else :
            tempNode = self.head
            while tempNode :
                if tempNode.value== nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            if tempNode == self.tail.next :
                return "The Node does not exists"

    def deleteCSLL(self, location ):
        if self.head is None :
            print("The CSLL is empty")
        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head.next = None
                    self.head = self.tail= None

                else :
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1 :
                if self.head == self.tail :
                    self.head.next = None
                    self.head = self.tail = None
                else :
                    tempNode = self.head
                    while tempNode :
                        if tempNode.next == self.tail :
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail =tempNode

            else :
                tempNode = self.head
                index = 0
                while index< location -1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        if self.head == None :
            return "The CSLL does not exists"
        else :
            self.head = None
            self.tail.next = None
            self.tail = None

if __name__ == '__main__' :

    circularSSL = CircularSinglyLinkedList()
    circularSSL.createCSLL(1)
    circularSSL.insertCSLL(0,0)
    circularSSL.insertCSLL(3,1)
    circularSSL.insertCSLL(5,-1)
    circularSSL.insertCSLL(2,2)
    circularSSL.insertCSLL(1,1)
    print([node.value for node in circularSSL])
    # circularSSL.traverseCSLL()

    print(circularSSL.searchCSLL(3))

    circularSSL.deleteCSLL(1)
    print([node.value for node in circularSSL])
    circularSSL.deleteEntireCSLL()
    print([node.value for node in circularSSL])

    # help(CircularSinglyLinkedList.insertCSLL)