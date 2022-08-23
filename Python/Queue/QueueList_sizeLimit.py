

class Queue(object):
    def __init__(self,maxSize):
        self.items = maxSize *[None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        values = [str(x) for x in self.items if x]
        return ' '.join(values)
    
    def isFull(self):
        if self.rear+1 == self.front :
            return True
        elif self.front == 0 and self.rear +1 == self.maxSize:
            return True
        else :
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else :
            return False

    def enqueue(self,value):
        if self.isFull():
            return "The Queue is full"
        else :
            if self.rear +1 == self.maxSize :
                self.rear = 0
            else :
                self.rear += 1
                if self.front == -1:
                    self.front = 0 
            self.items[self.rear] = value
            return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            firstElement = self.items[self.front]
            front = self.front
            if self.front == self.rear :
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front  = 0
            else :
                self.front += 1
            self.items[front] = None
            return firstElement
    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else :
            return self.items[self.front]

    def delete(self):
        self.items = self.maxSize *[None]
        self.front = -1
        self.rear = -1

    

customQueue = Queue(3)
print(customQueue.enqueue(34))
print(customQueue.enqueue(9))
print(customQueue.enqueue(8))
print(customQueue.enqueue(4))
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)