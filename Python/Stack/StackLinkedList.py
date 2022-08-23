

# Stack using Linked Lists

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode= curNode.next

class Stack :
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None :
            return True
        else :
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else :
            nodeValue = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue.value

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else :
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(55)
customStack.push(25)
customStack.push(35)
customStack.push(45)
print(customStack)
print("----------------------")
print(customStack.peek())
print("----------------------")
print(customStack.pop())
print("----------------------")
print(customStack)
print("----------------------")
print(customStack.isEmpty())
customStack.delete()
print("----------------------")
print(customStack.isEmpty())