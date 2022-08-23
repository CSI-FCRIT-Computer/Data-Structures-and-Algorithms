

class Node(object) :
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None :
            self.head = newNode
            self.tail = newNode
        else :
            if location == 0 :
                newNode.next = self.head
                self.head = newNode
            elif location == -1 :
                # newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else :
                tempNode = self.head
                index = 0
                while index<location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSSL(self):
        if self.head == None :
            print("The Singly Linked List does not exist")
        else :
            node = self.head
            while node :
                print (node.value)
                node = node.next

    def searchSSL(self, nodeValue):
        if self.head == None:
            print("The SSL is empty")
        else :
            node = self.head
            while node :
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    def deleteNode(self, location):
        if self.head == None :
            print("The Singly linked list does not exist")

        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head = self.tail= None
                else :
                    self.head = self.head.next
            elif location == -1 :
                if self.head == self.tail :
                    self.head = self.tail= None
                else :
                    tempNode = self.head
                    while tempNode :
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else :
                tempNode = self.head
                index = 0
                while index < location -1 :
                    tempNode  = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSSL(self):
        if self.head == None :
            print("The Linked List Does not exists")
        else:
            self.head = self.tail = None


if __name__ == '__main__' :

    singlyLinkedList = SLinkedList()
    singlyLinkedList.insertSLL(1,1)
    singlyLinkedList.insertSLL(13,1)
    singlyLinkedList.insertSLL(18,1)
    singlyLinkedList.insertSLL(16,-1)
    singlyLinkedList.insertSLL(11,1)

    print([node.value for node in singlyLinkedList])
    singlyLinkedList.traverseSSL()
    # print(singlyLinkedList.searchSSL(11))
    singlyLinkedList.deleteNode(3)
    print([node.value for node in singlyLinkedList])

    singlyLinkedList.deleteEntireSSL()
    print([node.value for node in singlyLinkedList])