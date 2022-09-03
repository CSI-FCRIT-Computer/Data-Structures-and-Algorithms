package com.stack;

import java.util.ArrayDeque;

public class ArrayDequeStack {
    public static void main(String[] args) {

        /*Creates a stack using ArrayDeque
             ArrayDeque<Type> name = new ArrayDeque<>();*/

        ArrayDeque<Integer> stack = new ArrayDeque<>();

        /*Add Elements
            add() - inserts the specified element at the end of the array deque
            addFirst() - inserts the specified element at the beginning of the array deque
            addLast() - inserts the specified at the end of the array deque
        */
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println(stack);
        stack.add(40);
        stack.addFirst(00);
        stack.addLast(50);
        System.out.println(stack);

        /*Peek or to access the elements
            getFirst() - returns the first element of the array deque
            getLast() - returns the last element of the array deque
            peek() - returns the first element of the array deque
            peekFirst() - returns the first element of the array deque
            peekLast() - returns the last element of the array deque
         */
        System.out.println(stack.peek());
        System.out.println(stack.peekFirst());
        System.out.println(stack.peekLast());
        System.out.println(stack.getFirst());
        System.out.println(stack.getLast());


        /*Pop or to remove elements
            remove() - returns and removes an element from the first element of the array deque
            remove(element) - returns and removes the specified element from the head of the array deque
            removeFirst() - returns and removes the first element from the array deque (equivalent to remove())
            removeLast() - returns and removes the last element from the array deque
            clear() - removes all elements from stack
         */

        System.out.println(stack.pop());
        System.out.println(stack.remove());
        System.out.println(stack.remove(1));
        System.out.println(stack.removeFirst());
        stack.clear();
    }
}
