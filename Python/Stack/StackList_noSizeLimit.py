# # Stack # #

# LIFO method 

# Stack using list without size limit

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):   # Time Complexiity --> amortized --> O(1)/O(n^2)
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else :
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else : 
            return self.list[-1] # or we can use self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None
    


customStack = Stack()
customStack.push(1)
customStack.push(7)
customStack.push(3)
customStack.push(5)
print(customStack)
print(customStack.isEmpty())
print(customStack.peek())
print(customStack.pop())
print(customStack)
customStack.delete()
print(customStack.isEmpty())

