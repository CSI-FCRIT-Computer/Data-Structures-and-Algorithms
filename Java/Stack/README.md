# Stack
- The stack is a linear data structure that is used to store the collection of objects.
- It is based on Last-In-First-Out (LIFO). That is, elements are added to the top of the stack and removed from the top of the stack.


![Stack](https://techblogstation.com/wp-content/uploads/2019/11/Stack-Push-And-Pop.png)

## InBuilt java Class
- In Java, Stack is a class that falls under the Collection framework that extends the Vector class.
- The Stack class contains only the default constructor that creates an empty stack.
- The Java Stack class provides mainly five methods to perform these operations. Along with this, it also provides all the methods of the Java Vector class.

## Stack Using ArrayDeque
- To implement a LIFO (Last-In-First-Out) stacks in Java, it is recommended to use a deque over the Stack class.
- The ArrayDeque class is likely to be faster than the Stack class.
- Deque is a linear data structure that allows insertion and deletion from both ends. We can use this data structure to implement other linear data structures like stacks and queues. 
- We will allow insertion and deletion from just one common end of the Deque to implement a Stack
- To know more why to use ArrayDeque [Click Here](https://stackoverflow.com/questions/12524826/why-should-i-use-deque-over-stack)

*Stack --> prints 1, 2, 3*

*Deque --> prints 3, 2, 1* 
