class Node(object) :
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedLists :
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next
            if node == self.tail.next :
                break

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    def insertCDLL(self, value , location):
        if self.head is None :
            return "The CDLL does not exist"
        else :
            newNode = Node(value)
            if location == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode

            elif location == -1 :
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

            else :
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode

    def traverseCDLL(self):
        if self.head == None :
            print("The CDLL is empty")
        else :
            tempNode = self.head
            while tempNode :
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraverseCDLL(self):
        if self.head == None :
            print("The CDLL is empty")
        else :
            tempNode = self.tail
            while tempNode :
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        if self.head == None :
            return "The CDLL is empty"
        else :
            tempNode = self.head
            while tempNode :
                if tempNode.value == nodeValue:
                    return "YES"
                if tempNode == self.tail:
                    return "NO"
                tempNode = tempNode.next

    def deleteCDLL(self, location):
        if self.head == None :
            print("No node to delete")
        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head.next = self.head.prev = self.head = self.tail = None
                else :
                    self.head.prev = self.tail
                    self.tail.next = self.head.next
                    self.head = self.head.next

            elif location == -1 :
                if self.head == self.tail :
                    self.head.next = self.head.prev = self.head = self.tail = None
                else :
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head

            else :
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode = tempNode.next
                    index+= 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode


    def deleteEntireCDLL(self):
        if self.head == None:
            print("There is no node in CDLL")
        else :
            self.tail.next = None
            tempNode = self.head
            while tempNode :
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = self.tail = None

if __name__ == '__main__' :


    circularDLL = CircularDoublyLinkedLists()
    print(circularDLL.createCDLL(5))
    circularDLL.insertCDLL(0,0)
    circularDLL.insertCDLL(4,1)
    circularDLL.insertCDLL(6,-1)
    circularDLL.insertCDLL(9,2)
    print([node.value for node in circularDLL])

    circularDLL.traverseCDLL()
    print("===================================")
    circularDLL.reverseTraverseCDLL()

    print(circularDLL.searchCDLL(10))


    circularDLL.deleteCDLL(2)
    print([node.value for node in circularDLL])

    circularDLL.deleteEntireCDLL()
    print([node.value for node in circularDLL])