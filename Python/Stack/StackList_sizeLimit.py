
# Stack using list with size limit

class Stack :
    def __init__(self,maxSize ):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else :
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else :
            return False

    def push(self,value):   # Time Complexiity --> amortized --> O(1)/O(n^2)
        if self.isFull():
            return "The stack is full"
        else :
            self.list.append(value)
            return "The element has been sucessfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else :
            return self.list.pop()
            
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else : 
            return self.list[-1]

    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(10)
customStack.push(40)
customStack.push(20)
customStack.push(30)
print(customStack)
print("---------------------------------")
print(customStack.peek())
print(customStack.peek())
print("---------------------------------")
print(customStack.pop())
print("---------------------------------")
print(customStack)
customStack.delete()
print(customStack.isEmpty())