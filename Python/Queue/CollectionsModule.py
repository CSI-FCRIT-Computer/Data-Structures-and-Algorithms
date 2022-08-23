

from collections import deque

customQueue = deque(maxlen=3)

print(customQueue)
customQueue.append(3)
customQueue.append(4)
customQueue.append(1)
print(customQueue)
customQueue.append(7)
print(customQueue)
print(customQueue.popleft())
print(customQueue)
customQueue.clear()
print(customQueue)